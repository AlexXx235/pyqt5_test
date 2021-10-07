import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QRadioButton, QHBoxLayout,
                             QVBoxLayout, QLabel, QLineEdit, QGroupBox, QButtonGroup)


class ContactForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Contact Form')
        self.createTabBar()
        self.show()

    def createTabBar(self):
        # Create tab bar
        tab_bar = QTabWidget()

        # Create tabs
        self.profile_tab = QWidget()
        self.background_tab = QWidget()

        # Add tabs to tab bar
        tab_bar.addTab(self.profile_tab, 'Profile details')
        tab_bar.addTab(self.background_tab, 'Background')

        # Initialize tab widgets
        self.createProfileTab()
        self.createBackgroundTab()

        # Create main layout and add tab bar there
        main_h_box = QHBoxLayout()
        main_h_box.addWidget(tab_bar)

        self.setLayout(main_h_box)

    def createProfileTab(self):
        # Create labels and line edits
        name_label = QLabel('Name:')
        name_line = QLineEdit()

        address_label = QLabel('Address')
        address_line = QLineEdit()

        # Create radio button group
        sex_group_box = QGroupBox('Sex')

        male_rb = QRadioButton('Male')
        female_rb = QRadioButton('Female')

        # Create layouts
        rb_h_box = QHBoxLayout()
        rb_h_box.addWidget(male_rb)
        rb_h_box.addWidget(female_rb)

        sex_group_box.setLayout(rb_h_box)

        profile_v_box = QVBoxLayout()
        profile_v_box.addWidget(name_label)
        profile_v_box.addWidget(name_line)
        profile_v_box.addStretch()
        profile_v_box.addWidget(address_label)
        profile_v_box.addWidget(address_line)
        profile_v_box.addStretch()
        profile_v_box.addWidget(sex_group_box)

        self.profile_tab.setLayout(profile_v_box)

    def createBackgroundTab(self):
        # Create group box and set main layout
        background_group_box = QGroupBox('Highest Level Of Education')

        rb_v_box = QVBoxLayout()

        high_school_rb = QRadioButton('High School Diploma')
        associate_rb = QRadioButton("Associate's Degree")
        bachelor_rb = QRadioButton("Bachelor's Degree")
        master_rb = QRadioButton("Master's Degree")
        doctorate_rb = QRadioButton("Doctorate or Higher")

        rb_v_box.addWidget(high_school_rb)
        rb_v_box.addWidget(associate_rb)
        rb_v_box.addWidget(bachelor_rb)
        rb_v_box.addWidget(master_rb)
        rb_v_box.addWidget(doctorate_rb)

        background_group_box.setLayout(rb_v_box)

        background_h_box = QHBoxLayout()
        background_h_box.addWidget(background_group_box)

        self.background_tab.setLayout(background_h_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactForm()
    sys.exit(app.exec_())