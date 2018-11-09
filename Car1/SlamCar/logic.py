from Ui import Ui_MainWindow
import serial
import serial.tools.list_ports
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import binascii

from Communcate import Communcate
from DataBase import DataBase

class signal_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(signal_ui,self).__init__()  #继承自身父类   
        
        self.__ser = serial.Serial()
        self.setupUi(self)      
        self.link= Communcate() 
        
        #信号设置
        self.Open_Button.clicked.connect(self.port_connect)
        self.Close_Button.clicked.connect(self.port_close)
        
        self.speedEdit.updated.connect(self.__updateSpeed)
        self.angleEdit.updated.connect(self.__updateAngle)
        
        self.forwardButton.pressed.connect(self.__forward)
        self.forwardButton.realeased.connect(self.__reset)
        
    def port_connect(self):
        self.Show_label.setText("open serial success!")
        return self.link.connect()
       
    def port_close(self):
        self.Show_label.setText("close serial success!")
        return self.link.close()  
    
    def run():
       # self.__workLoop()
        pass
    
    def stop():
        pass
    
    
    def sendData(self,msg):       
        if (self.__ser.isOpen()):
            return self.link.send(msg)     
        else:
            self.port_connect()
            return self.link.send(msg)
            self.Show_label.setText("send failed !")

    
    
    def __reset(self):
        db = DataBase()
        db.cmdMsg = [0,0]
        
    def __workLoop():
        
    
    def __updateReceive():
        pass
    
    def __updateSpeed():    
        db = DataBase()
        
        db.feedbackMsg = [0,0]

    def __updateAngle():
        db = DataBase()
        
        db.feedbackMsg = [0,0]
    
    def __refreshLable(): 
        db = DataBase()
        
        
        pass
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
