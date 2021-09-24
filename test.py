import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class DataBasePretender(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 100, 100)
        self.displayButtons()
        self.show()

    def displayButtons(self):
        btn1 = QPushButton("1", self)
        btn2 = QPushButton("1", self)
        btn1.setGeometry(25, 10, 50, 20)
        btn2.setGeometry(25, 30, 50, 20)
        btn1.clicked.connect(self.handler1)
        btn2.clicked.connect(self.handler2)
        btn1.show()
        btn2.show()

    def handler1(self):
        self.db_connection = 'HOLY SHIIIIIIIT!!!!'

    def handler2(self):
        print(self.db_connection)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataBasePretender()
    sys.exit(app.exec_())