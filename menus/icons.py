import sys
import os
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton,
                             QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, Qt
import random


class IconWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('images/pyqt_logo.png'))
        self.displayContent()
        self.show()

    def displayContent(self):
        v_box = QVBoxLayout()

        title = QLabel('Click the button')
        title.setFont(QFont('Times New Roman', 18))
        title.setAlignment(Qt.AlignCenter)

        self.btn = QPushButton()
        self.btn.resize(400, 200)

        os.chdir('images/icons')

        self.btn.setIcon(QIcon(random.choice(os.listdir())))
        self.btn.setIconSize(QSize(100, 100))
        self.btn.clicked.connect(self.changeIcon)

        os.chdir('../../')

        v_box.addWidget(title)
        v_box.addWidget(self.btn)

        self.setLayout(v_box)

    def changeIcon(self):
        os.chdir('images/icons')
        self.btn.setIcon(QIcon(random.choice(os.listdir())))
        os.chdir('../../')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IconWindow()
    sys.exit(app.exec_())