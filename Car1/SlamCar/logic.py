from Ui import Ui_MainWindow
import serial
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
from  Communcate import Communcate

class signal_ui(QtWidgets.QMainWindow,Ui_MainWindow):
    
    def __init__(self):
        super(signal_ui,self).__init__()  #继承自身父类   
     
        self.setupUi(self)      
        self.link= Communcate() 
        
        #信号设置
        self.Open_Button.clicked.connect(self.port_connect)
        self.Close_Button.clicked.connect(self.port_close)
        self.Start_Button.clicked.connect(self.port_send)
        
    def port_connect(self):       
        return self.link.connect()
        #self.Show_label.setText("open serial success!")
       
    def port_close(self):
        return self.link.close()
        #self.Show_label.setText("close serial success!")
        
    def port_send(self):
        return self.link.send()
    
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
