import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLabel
from PyQt5.QtCore import Qt


class CheckBoxWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.displayCheckBox()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 400)
        self.setWindowTitle("CheckBox")
        self.show()

    def displayCheckBox(self):
        check_box1 = QCheckBox('Male', self)
        check_box2 = QCheckBox('Male again', self)
        check_box1.setGeometry(50, 100, 100, 50)
        check_box2.setGeometry(50, 200, 100, 50)
        check_box1.stateChanged.connect(self.stateChanged)
        check_box2.stateChanged.connect(self.stateChanged)
        check_box1.show()
        check_box2.show()

    def stateChanged(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            print(f"Selected: {sender.text()}")
        else:
            print(f"Deselected: {sender.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxWindow()
    sys.exit(app.exec_())