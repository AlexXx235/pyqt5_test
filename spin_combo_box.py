import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox,
                             QSpinBox, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class BillForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Launch bill")
        self.displayMealForms()
        self.show()

    def displayMealForms(self):
        title_info = QLabel()
        title_info.setText('Select what you have eaten:')
        title_info.setFont(QFont('Arial', 17))
        title_info.setAlignment(Qt.AlignCenter)

        lunch_list = ["egg", "turkey sandwich", "ham sandwich", "cheese",
                      "hummus", "yogurt", "apple", "banana", "orange", "waffle",
                      "baby carrots", "bread", "pasta", "crackers", "pretzels",
                      "pita chips", "coffee", "soda", "water"]

        meal_cmb1 = QComboBox()
        meal_cmb1.addItems(lunch_list)

        meal_cmb2 = QComboBox()
        meal_cmb2.addItems(lunch_list)

        self.cost_sb1 = QSpinBox()
        self.cost_sb2 = QSpinBox()
        self.cost_sb1.setRange(0, 100)
        self.cost_sb2.setRange(0, 100)
        self.cost_sb1.setPrefix('$')
        self.cost_sb2.setPrefix('$')
        self.cost_sb1.valueChanged.connect(self.calculate_bill)
        self.cost_sb2.valueChanged.connect(self.calculate_bill)

        self.total_cost = QLabel('Total: 0$')
        self.total_cost.setFont(QFont('Arial', 16))
        self.total_cost.setAlignment(Qt.AlignRight)

        h_box_1 = QHBoxLayout()
        h_box_1.addWidget(meal_cmb1)
        h_box_1.addWidget(self.cost_sb1)

        h_box_2 = QHBoxLayout()
        h_box_2.addWidget(meal_cmb2)
        h_box_2.addWidget(self.cost_sb2)

        v_box = QVBoxLayout()
        v_box.addWidget(title_info)
        v_box.addLayout(h_box_1)
        v_box.addLayout(h_box_2)
        v_box.addWidget(self.total_cost)

        self.setLayout(v_box)

    def calculate_bill(self):
        total_cost = self.cost_sb1.value() + self.cost_sb2.value()
        self.total_cost.setText(f'Total: {total_cost}$')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BillForm()
    sys.exit(app.exec_())



