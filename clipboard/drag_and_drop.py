import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class DragAndDrop(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Drag And Drop')
        self.setGeometry(100, 100, 500, 500)
        self.createWidgets()
        self.show()

    def createWidgets(self):
        icons = [
            'images/1.png',
            'images/2.png',
            'images/3.png',
            'images/4.png'
        ]

        icons_label = QLabel('ICONS')
        icons_list = QListWidget()
        icons_list.setAcceptDrops(True)
        icons_list.setDragEnabled(True)
        icons_list.setViewMode(QListWidget.IconMode)
        for icon in icons:
            item = QListWidgetItem()
            item.setText(icon)
            item.setIcon(QIcon(icon))
            icons_list.addItem(item)
        icons_list.setIconSize(QSize(50, 50))

        list_title = QLabel('LIST')
        items_list = QListWidget()
        items_list.setAcceptDrops(True)
        items_list.setDragEnabled(True)
        items_list.setAlternatingRowColors(True)

        grid = QGridLayout()
        grid.addWidget(icons_label, 0, 0)
        grid.addWidget(list_title, 0, 1)
        grid.addWidget(icons_list, 1, 0)
        grid.addWidget(items_list, 1, 1)

        self.setLayout(grid)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DragAndDrop()
    sys.exit(app.exec_())