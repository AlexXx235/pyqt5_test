import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QTableWidget, QMenu,
                             QInputDialog, QTableWidgetItem)


class SimpleTable(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Table')
        self.setMinimumSize(1000, 500)
        self.createTable()
        self.createMenu()

        self.item_text = None

        self.show()

    def createTable(self):
        self.table = QTableWidget(10, 10)
        self.table.setCurrentCell(0, 0)
        self.table.horizontalHeader().sectionDoubleClicked.connect(self.changeHeader)
        self.setCentralWidget(self.table)

    def createMenu(self):
        quit_act = QAction("Quit", self)
        quit_act.setShortcut('Ctrl+Q')
        quit_act.triggered.connect(self.close)
        # Create table menu actions
        self.add_row_above_act = QAction("Add Row Above", self)
        self.add_row_above_act.triggered.connect(self.addRowAbove)
        self.add_row_below_act = QAction("Add Row Below", self)
        self.add_row_below_act.triggered.connect(self.addRowBelow)
        self.add_col_before_act = QAction("Add Column Before", self)
        self.add_col_before_act.triggered.connect(self.addColumnBefore)
        self.add_col_after_act = QAction("Add Column After", self)
        self.add_col_after_act.triggered.connect(self.addColumnAfter)
        self.delete_row_act = QAction("Delete Row", self)
        self.delete_row_act.triggered.connect(self.deleteRow)
        self.delete_col_act = QAction("Delete Column", self)
        self.delete_col_act.triggered.connect(self.deleteColumn)
        self.clear_table_act = QAction("Clear All", self)
        self.clear_table_act.triggered.connect(self.clearTable)
        # Create the menu bar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        # Create file menu and add actions
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(quit_act)
        # Create table menu and add actions
        table_menu = menu_bar.addMenu('Table')
        table_menu.addAction(self.add_row_above_act)
        table_menu.addAction(self.add_row_below_act)
        table_menu.addSeparator()
        table_menu.addAction(self.add_col_before_act)
        table_menu.addAction(self.add_col_after_act)
        table_menu.addSeparator()
        table_menu.addAction(self.delete_row_act)
        table_menu.addAction(self.delete_col_act)
        table_menu.addSeparator()
        table_menu.addAction(self.clear_table_act)

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        context_menu.addAction(self.add_row_above_act)
        context_menu.addAction(self.add_row_below_act)
        context_menu.addSeparator()
        context_menu.addAction(self.add_col_before_act)
        context_menu.addAction(self.add_col_after_act)
        context_menu.addSeparator()
        context_menu.addAction(self.delete_row_act)
        context_menu.addAction(self.delete_col_act)
        context_menu.addSeparator()
        copy_act = context_menu.addAction("Copy")
        paste_act = context_menu.addAction("Paste")
        context_menu.addSeparator()
        context_menu.addAction(self.clear_table_act)

        action = context_menu.exec_(self.mapToGlobal(event.pos()))
        if action == copy_act:
            self.copyItem()
        if action == paste_act:
            self.pasteItem()

    def changeHeader(self):
        col = self.table.currentColumn()

        text, ok = QInputDialog.getText(self, 'Enter Header', 'Header Text:')
        if ok and text != '':
            self.table.setHorizontalHeaderItem(col, QTableWidgetItem(text))
        else:
            pass

    def copyItem(self):
        if self.table.currentItem() != None:
            self.item_text = self.table.currentItem().text()

    def pasteItem(self):
        if self.item_text != '':
            row = self.table.currentRow()
            col = self.table.currentColumn()
            self.table.setItem(row, col, QTableWidgetItem(self.item_text))

    def addRowAbove(self):
        row = self.table.currentRow()
        self.table.insertRow(row)

    def addRowBelow(self):
        current_row = self.table.currentRow()
        self.table.insertRow(current_row + 1)

    def addColumnBefore(self):
        current_col = self.table.currentColumn()
        self.table.insertColumn(current_col)

    def addColumnAfter(self):
        current_col = self.table.currentColumn()
        self.table.insertColumn(current_col + 1)

    def deleteRow(self):
        current_row = self.table.currentRow()
        self.table.removeRow(current_row)

    def deleteColumn(self):
        current_col = self.table.currentColumn()
        self.table.removeColumn(current_col)

    def clearTable(self):
        self.table.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleTable()
    sys.exit(app.exec_())
