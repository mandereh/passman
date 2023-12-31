# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passman.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1259, 894)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 160, 751, 80))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 20, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.label.setObjectName("label")
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(360, 290, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.usernameInput.setFont(font)
        self.usernameInput.setText("")
        self.usernameInput.setObjectName("usernameInput")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(250, 290, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.demarcatorLine = QtWidgets.QFrame(self.centralwidget)
        self.demarcatorLine.setGeometry(QtCore.QRect(590, 270, 20, 241))
        self.demarcatorLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.demarcatorLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.demarcatorLine.setObjectName("demarcatorLine")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(250, 340, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(360, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.passwordInput.setFont(font)
        self.passwordInput.setObjectName("passwordInput")
        self.websiteSubmitInput = QtWidgets.QLineEdit(self.centralwidget)
        self.websiteSubmitInput.setGeometry(QtCore.QRect(358, 400, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.websiteSubmitInput.setFont(font)
        self.websiteSubmitInput.setObjectName("websiteSubmitInput")
        self.websiteSubmit = QtWidgets.QLabel(self.centralwidget)
        self.websiteSubmit.setGeometry(QtCore.QRect(250, 400, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.websiteSubmit.setFont(font)
        self.websiteSubmit.setObjectName("websiteSubmit")
        self.keyword = QtWidgets.QLabel(self.centralwidget)
        self.keyword.setGeometry(QtCore.QRect(250, 460, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.keyword.setFont(font)
        self.keyword.setObjectName("keyword")
        self.keywordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.keywordInput.setGeometry(QtCore.QRect(360, 460, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.keywordInput.setFont(font)
        self.keywordInput.setObjectName("keywordInput")
        self.websiteSearch = QtWidgets.QLabel(self.centralwidget)
        self.websiteSearch.setGeometry(QtCore.QRect(640, 290, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.websiteSearch.setFont(font)
        self.websiteSearch.setObjectName("websiteSearch")
        self.websiteSearchInput = QtWidgets.QLineEdit(self.centralwidget)
        self.websiteSearchInput.setGeometry(QtCore.QRect(740, 290, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.websiteSearchInput.setFont(font)
        self.websiteSearchInput.setObjectName("websiteSearchInput")
        self.passcodeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passcodeInput.setGeometry(QtCore.QRect(740, 340, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.passcodeInput.setFont(font)
        self.passcodeInput.setObjectName("passcodeInput")
        self.passcode = QtWidgets.QLabel(self.centralwidget)
        self.passcode.setGeometry(QtCore.QRect(640, 340, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.passcode.setFont(font)
        self.passcode.setObjectName("passcode")
        self.outputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.outputBox.setGeometry(QtCore.QRect(642, 390, 291, 101))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        self.outputBox.setFont(font)
        self.outputBox.setObjectName("outputBox")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(810, 520, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(430, 520, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1259, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        """my codes
        """
        self.submitButton.clicked.connect(self.submit)
        self.searchButton.clicked.connect(self.search)
        self.statusbar.setObjectName("statusbar")
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passcodeInput.setEchoMode(QtWidgets.QLineEdit.Password)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """mycode
        """
    def submit(self):
        print('clicked submit')
        username = self.usernameInput.text()
        password = self.passwordInput.text()
        submit_website = self.websiteSubmitInput.text()
        keyword = self.keywordInput.text()
        print(username,password,submit_website,keyword)
        has_number = False
        has_uppercase_char = False
        
    def search(self):
        print('clicked search')
        passcode = self.passcodeInput.text()
        search_website = self.websiteSearchInput.text()
        print(passcode, search_website)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " PASSWORD MANAGER"))
        self.username.setText(_translate("MainWindow", "Username"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.websiteSubmit.setText(_translate("MainWindow", "Website"))
        self.keyword.setText(_translate("MainWindow", "Keyword"))
        self.websiteSearch.setText(_translate("MainWindow", "Website"))
        self.passcode.setText(_translate("MainWindow", "Passcode"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
