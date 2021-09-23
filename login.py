import sys, json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCheckBox, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.displayTitle()
        self.displayLoginForm()
        self.displayPasswordForm()
        self.displayCheckBox()
        self.displayLoginButton()
        self.displaySignUpLabel()
        self.displaySignUpButton()

    def initializeUI(self):
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 400)
        self.show()

    def displayTitle(self):
        title = QLabel(self)
        title.setGeometry(150, 50, 100, 40)
        title.setText("Login")
        title.setFont(QFont('Arial', 20))
        title.setAlignment(Qt.AlignCenter)
        title.show()

    def displayLoginForm(self):
        login_label = QLabel(self)
        login_label.move(50, 150)
        login_label.setText("Login:")
        login_label.adjustSize()
        login_label.show()

        self.login_edit = QLineEdit(self)
        self.login_edit.setGeometry(120, 150, 160, 20)
        self.login_edit.setPlaceholderText("enter your login")
        self.login_edit.show()

    def displayPasswordForm(self):
        password_label = QLabel(self)
        password_label.move(50, 200)
        password_label.setText("Password:")
        password_label.adjustSize()
        password_label.show()

        self.password_edit = QLineEdit(self)
        self.password_edit.setGeometry(120, 200, 160, 20)
        self.password_edit.setPlaceholderText("enter your password")
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.show()

    def displayCheckBox(self):
        pwd_visible_cb = QCheckBox("show password", self)
        pwd_visible_cb.move(120, 230)
        pwd_visible_cb.stateChanged.connect(self.passwordShowMode)
        pwd_visible_cb.show()

    def passwordShowMode(self, state):
        if state == Qt.Checked:
            self.password_edit.setEchoMode(QLineEdit.Normal)
        else:
            self.password_edit.setEchoMode(QLineEdit.Password)

    def displayLoginButton(self):
        login_btn = QPushButton("Login", self)
        login_btn.setGeometry(150, 270, 100, 40)
        login_btn.clicked.connect(self.clickLogin)
        login_btn.show()

    def clickLogin(self):
        login = self.login_edit.text()
        password = self.password_edit.text()
        if login == '' or password == '':
            QMessageBox.warning(self, "Login failed", "Login or password can not be empty",
                                QMessageBox.Cancel, QMessageBox.Cancel)
            return
        filename = "users.txt"
        try:
            file = open(filename, 'r')
            users = json.load(file)
            file.close()
        except FileNotFoundError:
            QMessageBox.critical(self, "Login Failed!",
                                 "Database connection is failed. Try later.",
                                 QMessageBox.Cancel, QMessageBox.Cancel)
            return
        else:
            if users.get(login) == password:
                QMessageBox.information(self, "Login Successful!", f"Welcome, {login}",
                                        QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "Login Failed!", f"Something wrong with login or password",
                                    QMessageBox.Ok, QMessageBox.Ok)

    def displaySignUpLabel(self):
        sign_up_label = QLabel(self)
        sign_up_label.setText("Have no account?")
        sign_up_label.setGeometry(50, 350, 100, 20)
        sign_up_label.setFont(QFont('Arial', 6))
        sign_up_label.show()

    def displaySignUpButton(self):
        self.sign_up_btn = QPushButton("Sign up", self)
        self.sign_up_btn.setGeometry(170, 350, 60, 30)
        self.sign_up_btn.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
