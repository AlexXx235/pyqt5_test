import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction)
from PyQt5.QtCore import Qt, QSize


class StickyNotes(QMainWindow):
    note_id = 1
    notes = []

    def __init__(self):
        super(StickyNotes, self).__init__()
        self.initializeUI()
        StickyNotes.notes.append(self)

    def initializeUI(self):
        self.setWindowTitle('Note')
        self.setMinimumSize(QSize(250, 250))

        self.central_widget = QTextEdit()
        self.setCentralWidget(self.central_widget)

        self.createMenu()
        self.createClipboard()
        self.show()

    def createMenu(self):
        menu_bar = self.menuBar()

        # File Menu
        file_menu = menu_bar.addMenu('File')

        new_act = QAction('New', self)
        new_act.setShortcut('Ctrl+N')
        new_act.triggered.connect(self.newNote)

        clear_act = QAction('Clear', self)
        clear_act.setShortcut('Ctrl+W')
        clear_act.triggered.connect(self.clearNote)

        quit_act = QAction('Quit', self)
        quit_act.setShortcut('Ctrl+Q')
        quit_act.triggered.connect(self.close)

        file_menu.addAction(new_act)
        file_menu.addAction(clear_act)
        file_menu.addSeparator()
        file_menu.addAction(quit_act)

        # Color Menu
        color_menu = menu_bar.addMenu('Color')

        red_act = QAction('Red', self)
        red_act.triggered.connect(
            lambda: self.central_widget.setStyleSheet(
                'background-color: red'
            )
        )

        green_act = QAction('Green', self)
        green_act.triggered.connect(
            lambda: self.central_widget.setStyleSheet(
                'background-color: green'
            )
        )

        color_menu.addAction(red_act)
        color_menu.addAction(green_act)

        # Paste Menu
        paste_menu = menu_bar.addMenu('Paste')

        paste_act = QAction('Paste', self)
        paste_act.setShortcut('Ctrl+V')
        paste_act.triggered.connect(self.pasteFromClipboard)

        paste_menu.addAction(paste_act)

    def createClipboard(self):
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.pasteFromClipboard)

    def newNote(self):
        StickyNotes().show()
        StickyNotes.note_id += 1

    def clearNote(self):
        self.central_widget.clear()

    def pasteFromClipboard(self):
        self.central_widget.insertPlainText(self.clipboard.text() + '\n')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StickyNotes()
    sys.exit(app.exec_())