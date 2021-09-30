import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox,
                             QSpinBox, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRegExp


class BillForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()
        self.meal_count = 0
        self.lunch_dict = {"---": 0, "egg": 10, "turkey sandwich": 15,
                      "ham sandwich": 20, "cheese": 5,
                      "hummus": 10, "yogurt": 3, "apple": 1}

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

        self.add_meal_btn = QPushButton('Add meal')
        self.add_meal_btn.clicked.connect(self.add_meal)

        self.total_cost = QLabel('Total: 0$')
        self.total_cost.setFont(QFont('Arial', 16))
        self.total_cost.setAlignment(Qt.AlignRight)

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(title_info)
        self.v_box.addWidget(self.add_meal_btn)
        self.v_box.addWidget(self.total_cost)

        self.setLayout(self.v_box)

    def add_meal(self):
        self.meal_count += 1

        meal_cmb = QComboBox()
        meal_cmb.setObjectName(f'meal_cmb_{self.meal_count}')
        meal_cmb.addItems(self.lunch_dict.keys())
        meal_cmb.currentTextChanged.connect(self.calculate_bill)

        meal_cost = QLabel('---')
        meal_cost.setAlignment(Qt.AlignCenter)
        meal_cost.setObjectName(f'meal_cost_{self.meal_count}')

        meal_cmb.label = meal_cost

        h_box = QHBoxLayout()
        h_box.setObjectName(f'meal_h_box_{self.meal_count}')
        h_box.addWidget(meal_cmb)
        h_box.addWidget(meal_cost)

        self.v_box.insertLayout(self.v_box.count() - 2, h_box)

    def calculate_bill(self):
        sender = self.sender()
        cost = self.lunch_dict[sender.currentText()]
        sender.label.setText(f'{cost}$')

        children = self.findChildren(QLabel, QRegExp('meal_cost_*'))
        costs = [int(child.text()[:-1]) for child in children]
        total_cost = sum(costs)
        self.total_cost.setText(f'Total: {total_cost}$')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BillForm()
    sys.exit(app.exec_())
