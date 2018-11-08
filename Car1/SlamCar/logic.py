from Ui import Ui_MainWindow
import serial
import serial.tools.list_ports
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
from  Communcate import Communcate
import binascii
class signal_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(signal_ui,self).__init__()  #继承自身父类   
        
        self.__ser = serial.Serial()
        self.setupUi(self)      
        self.link= Communcate() 
        
        #信号设置
        self.Open_Button.clicked.connect(self.port_connect)
        self.Close_Button.clicked.connect(self.port_close)
        self.Start_Button.clicked.connect(self.port_send)
        
    def port_connect(self):
        self.Show_label.setText("open serial success!")
        return self.link.connect()
       
    def port_close(self):
        self.Show_label.setText("close serial success!")
        return self.link.close()  


    def port_send(self,msg):
        self.__write(self)      
        if (self.__ser.isOpen()):
            return self.link.send(msg)     
        else:
            self.__ser.open()
            return self.link.send(msg)
            self.Show_label.setText("send failed !")
   
    def __write(self,data):
        if (self.__ser.is_open()):           
            self.__ser.write(self.Speed_lineEdit.text().encode('utf-8'))
            self.__ser.write(self.Angle_lineEdit.text().encode('utf-8')) 
            self.__ser.write(self.Hight_lineEdit.text().encode('utf-8'))
        else:
            self.__ser.open()
            self.__ser.write(self.Speed_lineEdit.text().encode('utf-8'))
            self.__ser.write(self.Angle_lineEdit.text().encode('utf-8')) 
            self.__ser.write(self.Hight_lineEdit.text().encode('utf-8'))
    def port_read(self): 
        pass
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
