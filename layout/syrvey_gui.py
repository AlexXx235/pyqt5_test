import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class SurveyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Survey")
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        title = QLabel("University")
        title.setFont(QFont('Arial', 17))
        title.setAlignment(Qt.AlignCenter)

        title_h_box = QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()

        question = QLabel("How many classes have you had today?")
        question.setAlignment(Qt.AlignCenter)

        quantity_labels = ["What classes?", "I am ok", "Dork", "Beast"]
        cb_labels_h_box = QHBoxLayout()
        cb_labels_h_box.setSpacing(60)
        cb_labels_h_box.addStretch()
        for label in quantity_labels:
            cb_label = QLabel(label)
            cb_labels_h_box.addWidget(cb_label)
        cb_labels_h_box.addStretch()

        quantities = ['0', '1', '2', '>=3']
        cb_group_box = QButtonGroup()
        cb_h_box = QHBoxLayout()
        cb_h_box.setSpacing(70)
        cb_h_box.addStretch()
        for q in quantities:
            cb = QCheckBox(q)
            cb_group_box.addButton(cb)
            cb_h_box.addWidget(cb)
        cb_h_box.addStretch()

        cb_group_box.buttonClicked.connect(self.cb_clicked)

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)

        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(cb_labels_h_box)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(2)
        v_box.addWidget(close_btn)

        self.setLayout(v_box)

    def cb_clicked(self, state):
        print(state)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SurveyWindow()
    sys.exit(app.exec_())