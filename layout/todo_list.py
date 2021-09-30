import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit,
QLineEdit, QPushButton, QCheckBox, QGridLayout, QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('ToDo list')
        self.displayGrid()
        self.show()

    def displayGrid(self):
        title = QLabel('ToDo List')
        title.setFont(QFont('Arial', 18))
        title.setAlignment(Qt.AlignCenter)

        must_list_grid = QGridLayout()
        must_list_grid.setContentsMargins(5, 5, 5, 5)

        must_title = QLabel('Must Dos')
        must_title.setFont(QFont('Arial', 17))
        must_title.setAlignment(Qt.AlignCenter)

        for row in range(1, 15):
            cb = QCheckBox()
            cb.setChecked(False)
            le = QLineEdit()
            must_list_grid.addWidget(cb, row, 0)
            must_list_grid.addWidget(le, row, 1)

        appt_v_box = QVBoxLayout()
        appt_v_box.setContentsMargins(5, 5, 5, 5)

        appt_title = QLabel('Appointments')
        appt_title.setFont(QFont('Arial', 17))
        appt_title.setAlignment(Qt.AlignCenter)

        morning_title = QLabel('Morning')
        morning_title.setFont(QFont('Arial', 16))
        morning_title.setAlignment(Qt.AlignLeft)

        noon_title = QLabel('Noon')
        noon_title.setFont(QFont('Arial', 16))
        noon_title.setAlignment(Qt.AlignLeft)

        evening_title = QLabel('Evening')
        evening_title.setFont(QFont('Arial', 16))
        evening_title.setAlignment(Qt.AlignLeft)

        appt_v_box.addWidget(morning_title)
        appt_v_box.addWidget(QTextEdit())
        appt_v_box.addWidget(noon_title)
        appt_v_box.addWidget(QTextEdit())
        appt_v_box.addWidget(evening_title)
        appt_v_box.addWidget(QTextEdit())

        close_button = QPushButton('Close To Do List')
        close_button.clicked.connect(self.close)

        main_grid = QGridLayout()
        main_grid.addWidget(title, 0, 0, 1, 2)
        main_grid.addWidget(must_title, 1, 0)
        main_grid.addWidget(appt_title, 1, 1)
        main_grid.addLayout(must_list_grid, 2, 0)
        main_grid.addLayout(appt_v_box, 2, 1)
        main_grid.addWidget(close_button, 3, 0, 1, 2)

        self.setLayout(main_grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToDoList()
    sys.exit(app.exec_())