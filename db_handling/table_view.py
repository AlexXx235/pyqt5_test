import sys, csv
from PyQt5.QtWidgets import (QApplication, QWidget, QTableView, QVBoxLayout)
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Table')
        self.setGeometry(100, 100, 800, 500)
        self.createTable()
        self.show()

    def createTable(self):
        self.model = QStandardItemModel()

        table_view = QTableView()
        table_view.SelectionMode(3)
        table_view.setModel(self.model)

        self.model.setRowCount(2)
        self.model.setColumnCount(4)

        self.loadFromCSV()

        v_box = QVBoxLayout()
        v_box.addWidget(table_view)

        self.setLayout(v_box)

    def loadFromCSV(self):
        file = 'books.csv'
        with open(file, 'r') as f:
            reader = csv.reader(f)
            header_labels = next(reader)
            self.model.setHorizontalHeaderLabels(header_labels)
            for i, row in enumerate(reader):
                items = [QStandardItem(item) for item in row]
                self.model.insertRow(i, items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Table()
    sys.exit(app.exec_())