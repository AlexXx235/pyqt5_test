import sys
import json
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SignUpWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle("Registration")
        self.displayTitleLabel()
        self.displayInputForms()
        self.displaySingUpButton()
        self.show()

    def displayTitleLabel(self):
        title_label = QLabel(self)
        title_label.setGeometry(140, 30, 120, 40)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setText("Sign up")
        title_label.setFont(QFont('Arial', 18))
        title_label.show()

    def displayInputForms(self):
        login_label = QLabel("Login:", self)
        name_label = QLabel("Name:", self)
        password_label = QLabel("Password:", self)
        confirm_label = QLabel("Confirm:", self)

        login_label.setGeometry(50, 100, 100, 30)
        name_label.setGeometry(50, 150, 100, 30)
        password_label.setGeometry(50, 200, 100, 30)
        confirm_label.setGeometry(50, 250, 100, 30)

        login_label.show()
        name_label.show()
        password_label.show()
        confirm_label.show()

        self.login_edit = QLineEdit(self)
        self.name_edit = QLineEdit(self)
        self.password_edit = QLineEdit(self)
        self.confirm_edit = QLineEdit(self)

        self.login_edit.setGeometry(130, 100, 220, 30)
        self.name_edit.setGeometry(130, 150, 220, 30)
        self.password_edit.setGeometry(130, 200, 220, 30)
        self.confirm_edit.setGeometry(130, 250, 220, 30)

        self.login_edit.setPlaceholderText("enter login")
        self.name_edit.setPlaceholderText("firstname lastname")
        self.password_edit.setPlaceholderText("enter password")
        self.confirm_edit.setPlaceholderText("confirm password")

        self.password_edit.setEchoMode(QLineEdit.Password)
        self.confirm_edit.setEchoMode(QLineEdit.Password)

        self.login_edit.show()
        self.name_edit.show()
        self.password_edit.show()
        self.confirm_edit.show()

    def displaySingUpButton(self):
        sign_up_btn = QPushButton("Sign up", self)
        sign_up_btn.setGeometry(150, 300, 100, 50)
        sign_up_btn.clicked.connect(self.registration)
        sign_up_btn.show()

    def registration(self):
        login = self.login_edit.text()
        name = self.name_edit.text()
        password = self.password_edit.text()
        confirm = self.confirm_edit.text()

        try:
            file = open('users.txt', 'r')
            users = json.load(file)
            file.close()
        except FileNotFoundError:
            QMessageBox.critical(self, "Sign up failed!",
                                 "Database is unavailable now!",
                                 QMessageBox.Cancel)
        else:
            if login == '' or name == '' or password == '' or confirm == '':
                QMessageBox.warning(self, "Sign up failed!",
                                    "No one field can be empty!",
                                    QMessageBox.Cancel)
            elif login in users:
                QMessageBox.warning(self, "Sign up failed!",
                                    "Login already taken!",
                                    QMessageBox.Cancel)
            elif password != confirm:
                QMessageBox.warning(self, "Sign up failed!",
                                    "Passwords must match!",
                                    QMessageBox.Cancel)
            else:
                try:
                    file = open('users.txt', 'w')
                    users[login] = password
                    json.dump(users, file)
                    file.close()
                    QMessageBox.information(self, "Sign up Successful!",
                                            f"Welcome, {login}",
                                            QMessageBox.Ok)
                except FileNotFoundError:
                    QMessageBox.critical(self, "Sign up failed!",
                                         "Database is unavailable now!",
                                         QMessageBox.Cancel)

    def closeEvent(self, event):
        quit_decision = QMessageBox.question(self, "Do you want to quit the program?",
                                             "Are you sure to quit?",
                                             QMessageBox.Yes | QMessageBox.No)
        if quit_decision == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignUpWindow()
    sys.exit(app.exec_())