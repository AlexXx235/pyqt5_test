import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import pyqtSignal, QObject, Qt


class SendSignal(QObject):
    change_color = pyqtSignal()


class ColorChanger(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Press arrow')
        self.setGeometry(100, 100, 200, 200)
        self.createLabel()
        self.show()

    def createLabel(self):
        self.index = 0
        self.direction = ''
        self.colors = ['red', 'green', 'blue', 'yellow', 'aqua', 'violet',
                       'purple', 'black', 'blue']

        self.label = QLabel()
        self.label.setStyleSheet(f'background-color: {self.colors[self.index]}')
        self.setCentralWidget(self.label)

        self.sig = SendSignal()
        self.sig.change_color.connect(self.changeBackground)

    def keyPressEvent(self, key):
        if key.key() == Qt.Key_Up:
            self.direction = 'up'
        elif key.key() == Qt.Key_Down:
            self.direction = 'down'
        self.sig.change_color.emit()

    def changeBackground(self):
        if self.direction == 'up' and self.index < len(self.colors) - 1:
            self.index += 1
            self.label.setStyleSheet(f'background-color: {self.colors[self.index]}')
        elif self.direction == 'down' and self.index > 0:
            self.index -= 1
            self.label.setStyleSheet(f'background-color: {self.colors[self.index]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChanger()
    sys.exit(app.exec_())