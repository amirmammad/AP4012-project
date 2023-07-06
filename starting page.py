import sys
import typing
from time import sleep
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.uic import loadUi
import mysql.connector as myc

class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage,self).__init__()
        loadUi("login-page.ui",self)
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.go_signup)
    
    def login(self):
        username = self.username_line.text()
        password = self.password_line.text()
        db = myc.connect(host="127.0.0.1", user="root", password="", db="ap4022")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user_list WHERE username='"+ username +"' and password='"+ password +"'")
        result = cursor.fetchone()
        self.username_line.setText("")
        self.password_line.setText("")
        if result:
            self.logo.setText('')
            #go for main
        else:
            self.logo.setText('!')
    
    def go_signup(self):
        widget.setCurrentIndex(1)

class SignupPage(QDialog):
    def __init__(self):
        super(SignupPage,self).__init__()
        loadUi("signup-page.ui",self)
        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.go_login)
    
    def signup(self):
        username = self.username_line.text()
        password = self.password_line.text()
        email = self.email_line.text()
        db = myc.connect(host="127.0.0.1", user="root", password="", db="ap4022")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM user_list WHERE username='"+ username +"'")
        result = cursor.fetchone()
        if result:
            self.login_question.setText("you have an account lets")
        else:
            cursor.execute("INSERT INTO user_list values('"+ username +"','"+ password +"','"+ email +"','"+ '' +"')")
            db.commit()
            self.login_question.setText("signed up successfully, so")

    def go_login(self):
        widget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_page = LoginPage()
    signup_page = SignupPage()
    widget.addWidget(login_page)
    widget.addWidget(signup_page)
    widget.setCurrentIndex(0)
    widget.setFixedHeight(380)
    widget.setFixedWidth(720)
    widget.show()

    app.exec_()
