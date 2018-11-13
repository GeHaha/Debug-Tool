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
        self.communcate= Communcate() 
        
        #信号设置
        self.Open_Button.clicked.connect(self.port_connect)
        self.Close_Button.clicked.connect(self.port_close)
        
        self.Speed_lineEdit.textChanged.connect(self.__updateSpeed)
        self.Angle_lineEdit.textChanged.connect(self.__updateAngle)
        
        self.Start_Button.clicked.connect(self.run)
        self.Stop_Button.clicked.connect(self.stop)
        
        self.Front_Button.pressed.connect(self.forward)
        self.Front_Button.released.connect(self.reset)
        
        self.Back_Button.pressed.connect(self.back)
      #  self.Back_Button.realeased.connect(self._resback)
        
        self.Right_Button.pressed.connect(self.right)
     #   self.Right_Button.realeased.connect(self. __resright)
        
        self.Left_Button.pressed.connect(self.left)
       # self.Left_Button.pressed.connect(self.__releft)
        
    # connect port    
    def port_connect(self):
        self.communcate.connect()
        self.Show_label.setText("open serial success!")
    
    #close port
    def port_close(self):      
        self.communcate.close()  
        self.Show_label.setText("close serial success!")
    
   #send msg 
    def sendData(self,msg):
        self.communcate.__write()
        self.__ser.write(self.Angle_lineEdit.text())
        self.__ser.write(self.Speed_lineEdit.text())
        self.communcate.send(msg)     
    
    # let the car run
    def run(self):
       # self.__workLoop()
        pass
    
    # let the car stop
    def stop(self):
        pass
    # let the car go to head
    def forward(self):
        pass
    
    # let the car back
    def back(self):
        pass
  
    # let the car turn right
    def right(self):
        pass
    
    # let the car turn left
    def left(self):
        pass
    
    # when speed_lineEdit contants change ,the data while put into database
    def __updateSpeed(self):    
        db = DataBase()    
        db.feedbackMsg = [0,0]

    def __updateAngle(self):
        
        db = DataBase()        
        db.feedbackMsg = [0,0]
    
    #复位
    def __reset(self):
        db = DataBase()
        db.cmdMsg = [0,0]
        
    def __workLoop(self):
        pass
    
    def __updateReceive(self):
        db = DataBase()
     
    
    def __refreshLable(self): 
        db = DataBase()
        db.feedbackMsg = []
        for speed ,angle in db.feedbackMsg:
            speed = db.feedbackMsg [1:3]
            angle = db.feedbackMsg [2:6]
            
        self.Cur_speed_label.setText(speed)
        self.Cur_angle_label.setText(angle)
        
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = signal_ui()
    ui.show()
    sys.exit(app.exec_())
