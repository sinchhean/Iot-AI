import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 40, 50, 12))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 70, 131, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 170, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")




        self.pushButton.clicked.connect(self.A)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))
        self.pushButton_2.setText(_translate("Dialog", "PushButton"))

    def A(self,Dialog):
        try:
            Etext = self.lineEdit.text()
            _translate = QtCore.QCoreApplication.translate
            self.label.setText(_translate("Dialog",Etext))
        except:
            print(sys.exc_info())


class MyTimer(QWidget):
    def __init__(self, parent = None):
        super(MyTimer, self).__init__(parent)      
        self.resize(720, 640)      
        self.setWindowTitle("QTimerDemo")
            
        self.lcd = QLCDNumber()      
        self.lcd.setDigitCount(10)      
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(time.strftime("%X",time.localtime()))


        layout = QVBoxLayout()
        layout.addWidget(self.lcd)       
        self.setLayout(layout)
            
            
        self.timer = QBasicTimer() 
        self.timer.start(1000, self) 
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.move(50, 50)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.lcd.display(time.strftime("%X",time.localtime()))
        else:
            super(WigglyWidget, self).timerEvent(event)

                


app=QtWidgets.QApplication(sys.argv)
Form=QtWidgets.QWidget()
b = MyTimer()
ui=Ui_Dialog()
ui.setupUi(Form)
Form.show() 
if Form.show:
    ui.pushButton_2.clicked.connect(b.show)
    ui.pushButton_2.clicked.connect(Form.close)
b.myButton.clicked.connect(b.close)
b.myButton.clicked.connect(Form.show)
sys.exit(app.exec_())

