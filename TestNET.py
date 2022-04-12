import speedtest
from os import system
from pythonping import ping
from PyQt5 import QtCore, QtGui, QtWidgets
import psutil
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Test")
        #MainWindow.resize(776, 618)
        MainWindow.setFixedSize(776, 618)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("\n"
"QMainWindow{\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:0.738318, \n"
"    y2:0.444, stop:0 rgba(97, 72, 255, 255), stop:0.857955 rgba(113, 255, 255, 		255));\n"
"    \n"
"    \n"
"    \n"
"    \n"
"\n"
"}\n"
"QPushButton{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"    \n"
"\n"
"}\n"
"\n"
"\n"
"QLCDNumber{\n"
"    color:rgb(255, 255, 255);\n"
"    \n"
"    border:none;\n"
"    \n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"    \n"
"    \n"
"    background-color: #000000;\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"    \n"
"    \n"
"    \n"
"}\n"
"QLabel{\n"
"    background-color: #000000;\n"
"    background-color: rgba(0, 0, 0, 0.7);\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 480, 781, 101))
        self.groupBox.setStatusTip("")
        self.groupBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setVisible(False)
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton.setObjectName("radioButton")
        
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 67, 81, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(100, 0, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(560, 29, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 580, 781, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius: 10% 30% 50% 70%;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 781, 291))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelping = QtWidgets.QLabel(self.frame)
        self.labelping.setGeometry(QtCore.QRect(100, 160, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelping.setFont(font)
        self.labelping.setStyleSheet("background-color:none;")
        self.labelping.setObjectName("labelping")
        self.labelping_2 = QtWidgets.QLabel(self.frame)
        self.labelping_2.setGeometry(QtCore.QRect(350, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelping_2.setFont(font)
        self.labelping_2.setStyleSheet("background-color:none;")
        self.labelping_2.setObjectName("labelping_2")
        self.labelping_3 = QtWidgets.QLabel(self.frame)
        self.labelping_3.setGeometry(QtCore.QRect(630, 160, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelping_3.setFont(font)
        self.labelping_3.setStyleSheet("background-color:none;")
        self.labelping_3.setObjectName("labelping_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 60, 161, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:none;")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(350, 60, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:none;")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(630, 60, 141, 111))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none;")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 350, 241, 71))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border-radius: 30%;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    border-radius: none;\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(170, 255, 255);\n"
"\n"
"}")    
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.mn)#bt mn
        self.pushButton_2.clicked.connect(self.run)#bt run
        self.pushButton_3.clicked.connect(self.con)#bt connect
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TestNET", "TestNET"))
        self.groupBox.setToolTip(_translate("MainWindow", "<property name=\"visible\"><bool>false</bool</property>"))
        self.groupBox.setWhatsThis(_translate("MainWindow", "<property name=\"visible\">\n"
"   <bool>false</bool>\n"
"</property>"))
        self.radioButton.setText(_translate("MainWindow", "Disconnect"))
        self.radioButton_2.setText(_translate("MainWindow", "Connect"))
        self.label_4.setText(_translate("MainWindow", "Internet connection status"))
        self.pushButton_3.setText(_translate("MainWindow", "change"))
        self.label_5.setText(_translate("MainWindow", "'8.8.8.8' is used for ping test"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.labelping.setText(_translate("MainWindow", "Ping"))
        self.labelping_2.setText(_translate("MainWindow", "download"))
        self.labelping_3.setText(_translate("MainWindow", "upload"))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "..."))
        self.label_2.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "..."))
        self.label_3.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "..."))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))

    def mn(self):
        
        if  self.groupBox.isVisible():
                self.groupBox.hide()
                
        else:
                self.groupBox.show()
        




    def run(self):
        app.processEvents()
        print("please wait...")
        app.processEvents()
        response_list = ping('8.8.8.8', size=40, count=10)


        ping1 = (response_list.rtt_avg_ms)
        


        st = speedtest.Speedtest()
        mbd = st.download()
        mbu = st.upload()

        dow = ('%.1f' % float(mbd/1000000)) 
        upl = ('%.1f' % float(mbu/1000000)) 
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", f"{ping1}"))
        self.label_2.setText(_translate("MainWindow", f"{dow}"))
        self.label_3.setText(_translate("MainWindow", f"{upl}"))
        print("Ok")
        

    def con(self):
            _translate = QtCore.QCoreApplication.translate
            if self.radioButton_2.isChecked():
                    system("ipconfig /renew")
                    
                    app.processEvents()
                    #print("please wait...")
                    app.processEvents()
                    

            if self.radioButton.isChecked():
                    app.processEvents()
                    #print("please wait...")
                    app.processEvents()
                    system("ipconfig /release")
                    
                    

    
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
