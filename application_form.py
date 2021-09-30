import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QComboBox, QFormLayout, QTextEdit,
                             QSpinBox, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRegExp


class ApplicationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 300, 500)
        self.setWindowTitle('Application')
        self.displayForm()
        self.show()

    def displayForm(self):
        title = QLabel('Appointment Submission Form')
        title.setFont(QFont('Arial', 17))
        title.setAlignment(Qt.AlignCenter)

        name_le = QLineEdit()

        address_le = QLineEdit()

        phone_number_le = QLineEdit()
        phone_number_le.setInputMask('000-000-00-00')

        age_label = QLabel('Age')

        age = QSpinBox()
        age.setRange(0, 100)

        height_label = QLabel('Height')

        height = QLineEdit()
        height.setPlaceholderText('cm')

        weight_label = QLabel('Weight')
        weight = QLineEdit()
        weight.setPlaceholderText('kg')

        info_h_box = QHBoxLayout()
        info_h_box.addWidget(age_label)
        info_h_box.addWidget(age)
        info_h_box.addWidget(height_label)
        info_h_box.addWidget(height)
        info_h_box.addWidget(weight_label)
        info_h_box.addWidget(weight)

        gender = QComboBox()
        gender.addItems(['Male', 'Female'])

        surgeries = QTextEdit()
        surgeries.setPlaceholderText('separated by ;')

        blood_type = QComboBox()
        blood_type.addItems(['A', 'B', 'C', 'D'])

        hours = QSpinBox()
        hours.setRange(1, 12)

        minutes = QComboBox()
        minutes.addItems([':00', ':15', ':30', ':45'])

        postfix = QComboBox()
        postfix.addItems(['AM', 'PM'])

        time_h_box = QHBoxLayout()
        time_h_box.addWidget(hours)
        time_h_box.addWidget(minutes)
        time_h_box.addWidget(postfix)

        submit_btn = QPushButton('Submit Appointment')
        submit_btn.clicked.connect(self.close)

        form = QFormLayout()
        form.addRow(title)
        form.addRow('Name', name_le)
        form.addRow('Address', address_le)
        form.addRow('Mobile Number', phone_number_le)
        form.addRow(info_h_box)
        form.addRow('Gender', gender)
        form.addRow('Past surgeries', surgeries)
        form.addRow('Blood Type', blood_type)
        form.addRow('Desired Time', time_h_box)
        form.addRow(submit_btn)

        self.setLayout(form)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ApplicationForm()
    sys.exit(app.exec_())