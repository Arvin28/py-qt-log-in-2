
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox



class Ui_MainWindow(object):
        
        
            
    def setupUi(self, MainWindow):
        def file_save(self):
                file_name = QFileDialog.getSaveFileName(self,'save File')
                if file_name [0]:
                        f = open(file_name[0],'w')
                        
        
            
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -10, 511, 441))
        self.label_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_3.setStyleSheet("border-radius:5px;\n"
"border-color:white;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../2077a.png"))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.rigister_btn = QtWidgets.QPushButton(self.centralwidget)
        self.rigister_btn.setGeometry(QtCore.QRect(180, 310, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rigister_btn.setFont(font)
        self.rigister_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rigister_btn.setStyleSheet("background-color:green;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;")
        self.rigister_btn.setObjectName("rigister_btn")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(192, 210, 121, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("border-radius:5px;\n"
"border-color:white;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 140, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.forgot_pass_btn = QtWidgets.QPushButton(self.centralwidget)
        self.forgot_pass_btn.setGeometry(QtCore.QRect(160, 360, 201, 23))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.forgot_pass_btn.setFont(font)
        self.forgot_pass_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgot_pass_btn.setMouseTracking(False)
        self.forgot_pass_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.forgot_pass_btn.setAcceptDrops(False)
        self.forgot_pass_btn.setStyleSheet("border-radius:10px;\n"
"border-color:white;")
        self.forgot_pass_btn.setAutoExclusive(True)
        self.forgot_pass_btn.setAutoDefault(False)
        self.forgot_pass_btn.setDefault(False)
        self.forgot_pass_btn.setFlat(True)
        self.forgot_pass_btn.setObjectName("forgot_pass_btn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 210, 71, 20))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.log_in_btn = QtWidgets.QPushButton(self.centralwidget)
        self.log_in_btn.setGeometry(QtCore.QRect(180, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.log_in_btn.setFont(font)
        self.log_in_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.log_in_btn.setStyleSheet("background-color:blue;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.log_in_btn.setObjectName("log_in_btn")
        self.user_name = QtWidgets.QLineEdit(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(190, 140, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("border-radius:5px;\n"
"border-color:white;")
        self.user_name.setObjectName("user_name")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 20, 31, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 514, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.save_as = QtWidgets.QAction(MainWindow)
        self.save_as.setObjectName("save_as")
        self.save_all = QtWidgets.QAction(MainWindow)
        self.save_all.setObjectName("save_all")
        self.actionAbout_us = QtWidgets.QAction(MainWindow)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.exit = QtWidgets.QAction(MainWindow)
        self.exit.setObjectName("exit")
        self.about_app = QtWidgets.QAction(MainWindow)
        self.about_app.setObjectName("about_app")
        self.about_developer = QtWidgets.QAction(MainWindow)
        self.about_developer.setObjectName("about_developer")
        self.actionabout_your_mother = QtWidgets.QAction(MainWindow)
        self.actionabout_your_mother.setObjectName("actionabout_your_mother")
        self.menuFile.addAction(self.save_as)
        self.menuFile.addAction(self.save_all)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.exit)
        self.menuHelp.addAction(self.about_app)
        self.menuHelp.addAction(self.about_developer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        def dts(args):
                f = app.destroyed()
        
           
        
        
            


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome"))
        
        self.rigister_btn.setToolTip(_translate("MainWindow", "if you dont have account prees this"))
        self.rigister_btn.setText(_translate("MainWindow", "Rigister"))
        self.password.setToolTip(_translate("MainWindow", "ex:12321232"))
        self.label_2.setText(_translate("MainWindow", "Username :"))
        self.forgot_pass_btn.setToolTip(_translate("MainWindow", "if you forgot your account prees this"))
        self.forgot_pass_btn.setText(_translate("MainWindow", "i forgot my password"))
        self.label_5.setText(_translate("MainWindow", "Password :"))
        self.log_in_btn.setToolTip(_translate("MainWindow", "if you have account prees this"))
        self.log_in_btn.setText(_translate("MainWindow", "Log in"))
        self.user_name.setToolTip(_translate("MainWindow", "ex:arvin4838"))
        self.label_4.setText(_translate("MainWindow", "Hi"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.save_as.setText(_translate("MainWindow", "save as"))
        self.save_all.setText(_translate("MainWindow", "save all"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.about_app.setText(_translate("MainWindow", "about app"))
        self.about_developer.setText(_translate("MainWindow", "about developer"))
        
        
        
        
        
        
        
        # self.exit.triggered.connect(dt)
        
        

      
          
                        
                       
                
            
        # user1 = self.user_name
        # password1 = self.password
        
        
        
        
        
        
        
        # def saveFunc(self):
        #         name = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File',"Python Files (*.py)")
        #         name.setNameFilters(["*.py"])
        #         name.selectNameFilter("Python Files (*.py)")
        #         file = open(name, 'w')
                
        
        # def openFunc(self):
        #     name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        #     file = open(name, 'r')
        #     with file:
        #             deck = file.read()
        #             self.allCards.append(file.allCards)
                    
                    
            
        
        
       
       
        

        
            
if __name__ == "__main__":
        import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

            
        
        
        
        
        
        # def btns(self):
        #         if user1 == "Arvin2077" and password1 == "12345":
        #                 QMessageBox.about(self, "Success", "Welcome back:")
        #                 self.log_in_btn.clicked.connect(btns)
        #         else:
        #                 QMessageBox.about(self, "Failed", "i dont know who you are?:")
        #                 self.log_in_btn.clicked.connect(btns)
            
       
    

        


       

                
                



