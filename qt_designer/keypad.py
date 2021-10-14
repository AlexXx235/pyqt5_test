import sys
from keypad_gui import Ui_Keypad
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator

class Keypad(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Keypad()
        self.ui.setupUi(self)
        self.initializeUI()

    def initializeUI(self):
        self.initButtonActions()
        self.setLabelValidators()
        self.show()

    def setLabelValidators(self):
        self.ui.digit_1.setValidator(QIntValidator(0, 9))
        self.ui.digit_2.setValidator(QIntValidator(0, 9))
        self.ui.digit_3.setValidator(QIntValidator(0, 9))
        self.ui.digit_4.setValidator(QIntValidator(0, 9))

    def initButtonActions(self):
        self.ui.btn_0.clicked.connect(self.addDigit)
        self.ui.btn_1.clicked.connect(self.addDigit)
        self.ui.btn_2.clicked.connect(self.addDigit)
        self.ui.btn_3.clicked.connect(self.addDigit)
        self.ui.btn_4.clicked.connect(self.addDigit)
        self.ui.btn_5.clicked.connect(self.addDigit)
        self.ui.btn_6.clicked.connect(self.addDigit)
        self.ui.btn_7.clicked.connect(self.addDigit)
        self.ui.btn_8.clicked.connect(self.addDigit)
        self.ui.btn_9.clicked.connect(self.addDigit)
        self.ui.btn_hash.clicked.connect(self.checkPasscode)

    def addDigit(self):
        digits = self.ui.digit_frame.findChildren(QLineEdit, QRegExp('digit_\d'))
        for digit in digits:
            if digit.text() == '':
                digit.setText(self.sender().text())
                return

    def checkPasscode(self):
        passcode = ''
        digits = self.ui.digit_frame.findChildren(QLineEdit, QRegExp('digit_\d'))
        for digit in digits:
            if digit.text() == '':
                QMessageBox.critical(self, 'Error', 'There are empty boxes', QMessageBox.Ok)
                return
            else:
                passcode += digit.text()
            digit.clear()
        if passcode == '2486':
            QMessageBox.information(self, 'Success', 'Correct passcode', QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Fail', 'Incorrect passcode', QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Keypad()
    sys.exit(app.exec_())