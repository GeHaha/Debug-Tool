import serial
from SerialPack import DataPack
import DataBase
import struct
import time
from Ui import Ui_MainWindow
import serial
from PyQt5 import QtCore,QtGui,QtWidgets
import sys


class Communcate(QtWidgets.QMainWindow,Ui_MainWindow):
    """     
    communcate with mcu
    """
    __instance = None
    __isFirstInit = False
    
    def __new__(cls):
        if not cls.__instance:
            Communcate.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        super(Communcate,self).__init__()  
        if not self.__isFirstInit:    
            self.__connectState = False
            self.__ser = serial.Serial()
        else:
            pass
    
        self.__ser = serial.Serial()
        self.setupUi(self)

    def  __del__(self):
        self.__ser.close()
   
    
    def connect(self):
        self.__ser.baudrate = 115200
        self.__ser.port = "COM1"
        self.__ser.bytesize = serial.EIGHTBITS
        self.__ser.stopbits = serial.STOPBITS_ONE
        self.__ser.parity =  serial.PARITY_NONE
        self.__ser.open()
        if(self.__ser.isOpen()):
            print("open serial success")           
            return True
        else:
          print("open serial faild !!!")
          return False  

    def close(self):
        self.__ser.close()
                     
    # omit a single 
    def receive(self):
        data = self.__read()
        print("receive data", data)
        msg = DataPack()
        msg.setData(data)
        return msg

    def send(self, msg):          
        self.__write(msg.data())
       # self.__write(msg.data()) 
        
    def __read(self):
        res_data = ()
        while(self.__ser.is_open()):
            size = self.__ser.inWaiting()
            if size:
                # print(size) 
                res_data = self.__ser.read_all()
                # print("%X" %res_data[2])
                # print("%X" %res_data[3])
                return res_data
                self.__ser.flushInput()

    def __write(self,data):
        self.__ser.write(data)      
       
# def receive():
    #  while True:
        # msg = McuCommuncate.receive()
        # print(msg)
"""
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Communcate()
    ui.show()
    sys.exit(app.exec_())

# test this class
def test():
    data = [0x9c,0x03,0x10,0x50,0x08,0x10,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x07,0x01]
    msg = DataPack() 
    msg.setData(data)
    McuCommuncate = Communcate()

    if not McuCommuncate.connect():
        print("faile")
    while True:
        McuCommuncate.send(msg)
        time.sleep(1)
    # msg = McuCommuncate.receive()
    # print(msg.data())
test()
"""

