import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                             QRadioButton, QGroupBox, QTabWidget, QButtonGroup, QFormLayout, QSizePolicy,
                             QDesktopWidget)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize

style_sheet = """
    QWidget {
        background-color: #fff7bf;
    }
    QTabWidget {
        border: 1px solid #ffe100;
    }
    QLabel {
        background-color: #fff3a8;
    }
    QLabel#Image {
        border: 1px solid black;
    }
    QLabel#Description {
        background-color: #fff3a8;
        border: 1px solid #ffe100;
        border-radius: 8px;
        padding: 3px;
    }
    QLabel#Title {        
        background-color: #ffed66;
        border: 1px solid #ffe100;
        border-radius: 8px;
        padding: 3px;
    }
    QGroupBox {
        background-color: #fff3a8;
    }
    QRadioButton {
        background-color: #fff3a8;
    }
    QPushButton#AddBtn {
        background-color: #ffed66;
        border: 1px solid #ffe100;
        border-radius: 8px;
        padding: 5px;
    }
    QPushButton#AddBtn:hover {
        background-color: #ffe01c;
        border: 1px solid #ffe100;
        border-radius: 8px;
        padding: 5px;
    }
    QPushButton#AddBtn:pressed {
        background-color: #fff7bf;
    }
    #Order {
        padding: 8px;
        background-color: #fff3a8;
    }
"""

class FoodOrder(QWidget):
    image_size = QSize(100, 100)

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Food Order')
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.createTabBar()
        self.createOrderList()
        self.createMainLayout()
        self.setStyleSheet(style_sheet)
        self.show()
        self.centerMainWindow()

    def centerMainWindow(self):
        # Get screen W and H
        desktop = QDesktopWidget().screenGeometry()
        screen_width = desktop.width()
        screen_height = desktop.height()

        # Move to center
        self.move(int((screen_width - self.width()) / 2),
                  int((screen_height - self.height()) / 2))

    def createTabBar(self):
        # Create tab bar
        self.tab_bar = QTabWidget(self)
        self.tab_bar.setFixedWidth(400)

        # Create and add tabs widgets
        self.pizza_tab = QWidget()
        self.wings_tab = QWidget()

        self.tab_bar.addTab(self.pizza_tab, 'Pizza')
        self.tab_bar.addTab(self.wings_tab, 'Wings')

        # Initialize tabs
        self.createPizzaTab()
        self.createWingsTab()

    def createPizzaTab(self):
        # Main title
        pizza_title = QLabel('BUILD YOUR OWN PIZZA')
        pizza_title.setObjectName('Title')

        # Description block
        image = QPixmap('images/pizza.jpg').scaled(self.image_size)

        image_label = QLabel()
        image_label.setPixmap(image)
        image_label.setObjectName('Image')

        description = QLabel('Build a custom pizza for you. Start with '
                             'your favourite crust and add any toppings, '
                             'plus the perfect amount of cheese sauce.')
        description.setObjectName('Description')
        description.setWordWrap(True)

        title_h_box = QHBoxLayout()

        title_h_box.addWidget(image_label)
        title_h_box.addWidget(description)
        title_h_box.setAlignment(Qt.AlignCenter)

        crust_title = QLabel('CHOOSE YOUR CRUST')
        crust_title.setObjectName('Title')

        crust_rb_group = QGroupBox(self.pizza_tab)
        self.crust_buttons = QButtonGroup()

        crust_v_box = QVBoxLayout()

        crusts = [
            'Hand-Tossed',
            'Flat',
            'Stuffed'
        ]

        for crust in crusts:
            rb = QRadioButton(crust)
            crust_v_box.addWidget(rb)
            self.crust_buttons.addButton(rb)

        crust_rb_group.setLayout(crust_v_box)

        topping_title = QLabel('CHOOSE YOUR TOPPINGS')
        topping_title.setObjectName('Title')

        topping_rb_group = QGroupBox()
        self.topping_buttons = QButtonGroup()

        topping_v_box = QVBoxLayout()

        toppings = [
            'Pepperoni',
            'Sausage',
            'Bacon',
            'Canadian Bacon',
            'Beef',
            'Pineapple',
            'Mushroom',
            'Onion',
            'Olive',
            'Green Pepper',
            'Tomato',
            'Spinach',
            'Cheese'
        ]

        for topping in toppings:
            rb = QRadioButton(topping)
            topping_v_box.addWidget(rb)
            self.topping_buttons.addButton(rb)
        self.topping_buttons.setExclusive(False)

        topping_rb_group.setLayout(topping_v_box)

        add_btn = QPushButton('Add to order')
        add_btn.setObjectName('AddBtn')
        add_btn.clicked.connect(self.add_pizza_to_order)

        pizza_tab_v_box = QVBoxLayout()

        pizza_tab_v_box.addWidget(pizza_title)
        pizza_tab_v_box.addStretch()
        pizza_tab_v_box.addLayout(title_h_box)
        pizza_tab_v_box.addStretch()
        pizza_tab_v_box.addWidget(crust_title)
        pizza_tab_v_box.addStretch()
        pizza_tab_v_box.addWidget(crust_rb_group)
        pizza_tab_v_box.addStretch()
        pizza_tab_v_box.addWidget(topping_title)
        pizza_tab_v_box.addStretch()
        pizza_tab_v_box.addWidget(topping_rb_group)
        pizza_tab_v_box.addStretch()
        pizza_tab_v_box.addWidget(add_btn, alignment=Qt.AlignRight)

        pizza_tab_v_box.setAlignment(Qt.AlignTop)

        self.pizza_tab.setLayout(pizza_tab_v_box)

    def createWingsTab(self):
        wings_title = QLabel('TRY OUR AMAZING WINGS')
        wings_title.setObjectName('Title')

        wings_image = QPixmap('images/wings.jpg').scaled(self.image_size)

        wings_image_label = QLabel()
        wings_image_label.setPixmap(wings_image)
        wings_image_label.setObjectName('Image')

        wings_description = QLabel('6 pieces of rich-tasting, white meat '
                                   'chicken that will have you coming '
                                   'back for more.')
        wings_description.setObjectName('Description')
        wings_description.setWordWrap(True)

        wings_title_h_box = QHBoxLayout()
        wings_title_h_box.addWidget(wings_image_label)
        wings_title_h_box.addWidget(wings_description)
        wings_title_h_box.setAlignment(Qt.AlignCenter)

        flavor_title = QLabel('CHOOSE YOUR FLAVOR')
        flavor_title.setObjectName('Title')

        flavor_rb_group = QGroupBox()
        self.flavor_buttons = QButtonGroup()

        flavors = [
            'Buffalo',
            'Sweet-Sour',
            'Teriyaki',
            'Barbecue'
        ]

        flavors_cb_v_box = QVBoxLayout()

        for flavor in flavors:
            rb = QRadioButton(flavor)
            flavors_cb_v_box.addWidget(rb)
            self.flavor_buttons.addButton(rb)

        flavor_rb_group.setLayout(flavors_cb_v_box)

        add_btn = QPushButton('Add to order')
        add_btn.clicked.connect(self.add_wings_to_order)
        add_btn.setObjectName('AddBtn')

        wings_tab_v_box = QVBoxLayout()

        wings_tab_v_box.addWidget(wings_title)
        # wings_tab_v_box.addStretch()
        wings_tab_v_box.addLayout(wings_title_h_box)
        # wings_tab_v_box.addStretch()
        wings_tab_v_box.addWidget(flavor_title)
        # wings_tab_v_box.addStretch()
        wings_tab_v_box.addWidget(flavor_rb_group)
        # wings_tab_v_box.addStretch()
        wings_tab_v_box.addWidget(add_btn, alignment=Qt.AlignRight)

        wings_tab_v_box.setAlignment(Qt.AlignTop)

        self.wings_tab.setLayout(wings_tab_v_box)

    def createOrderList(self):
        self.order_list = QWidget()
        self.order_list.setFixedWidth(250)

        order_list_title = QLabel('YOUR ORDER')
        order_list_title.setObjectName('Title')
        order_list_title.setAlignment(Qt.AlignCenter)

        order_list_v_box = QVBoxLayout()
        order_list_v_box.addWidget(order_list_title)
        order_list_v_box.setAlignment(Qt.AlignTop)
        self.order_list.setLayout(order_list_v_box)

    def createMainLayout(self):
        main_layout = QHBoxLayout()
        self.tab_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        main_layout.addWidget(self.tab_bar)
        main_layout.addWidget(self.order_list)

        self.setLayout(main_layout)

    def add_pizza_to_order(self):
        crust_btn = self.crust_buttons.checkedButton()
        if crust_btn:
            toppings = [btn.text() for btn in self.topping_buttons.buttons() if btn.isChecked()]
            if toppings:
                toppings_label = QLabel(',\n'.join(toppings))
                toppings_label.setWordWrap(True)

                pizza_desc = QFormLayout()
                pizza_desc.addRow('Pizza type:', QLabel(crust_btn.text()))
                pizza_desc.addRow('Toppings:', toppings_label)

                v_box = QVBoxLayout()
                v_box.addWidget(QLabel('Pizza'), alignment=Qt.AlignCenter)
                v_box.addLayout(pizza_desc)

                pw = QWidget()
                pw.setObjectName('Order')
                pw.setLayout(v_box)

                self.order_list.layout().addWidget(pw)

    def add_wings_to_order(self):
        btn = self.flavor_buttons.checkedButton()
        if btn:
            label = QLabel(f'Wings: {btn.text()}')
            label.setObjectName('Order')
            self.order_list.layout().addWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FoodOrder()
    sys.exit(app.exec_())