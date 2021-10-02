import sys
import os
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QAction, QMessageBox,
                             QFileDialog, QColorDialog, QFontDialog, QInputDialog)
from PyQt5.Qt import QTextCursor, QColor, QIcon
from PyQt5.QtCore import Qt


class Notepad(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle('Notepad')
        self.displayTextEdit()
        self.displayMenu()
        self.show()

    def displayTextEdit(self):
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

    def getIconPath(self):
        return 'images/icons/' + random.choice(os.listdir('images/icons/'))

    def displayMenu(self):
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu('File')

        new_act = QAction(QIcon(self.getIconPath()), 'New', self)
        new_act.setShortcut('Ctrl+N')
        new_act.triggered.connect(self.clearText)
        file_menu.addAction(new_act)

        open_act = QAction(QIcon(self.getIconPath()), 'Open', self)
        open_act.setShortcut('Ctrl+O')
        open_act.triggered.connect(self.openNote)
        file_menu.addAction(open_act)

        save_act = QAction(QIcon(self.getIconPath()), 'Save', self)
        save_act.setShortcut('Ctrl+S')
        save_act.triggered.connect(self.saveNote)
        file_menu.addAction(save_act)

        file_menu.addSeparator()

        exit_act = QAction(QIcon(self.getIconPath()), 'Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)
        file_menu.addAction(exit_act)

        # Edit menu
        edit_menu = menu_bar.addMenu('Edit')

        undo_act = QAction(QIcon(self.getIconPath()), 'Undo', self)
        undo_act.setShortcut('Ctrl+Z')
        undo_act.triggered.connect(self.text_edit.undo)
        edit_menu.addAction(undo_act)

        redo_act = QAction(QIcon(self.getIconPath()), 'Redo', self)
        redo_act.setShortcut('Ctrl+Shift+Z')
        redo_act.triggered.connect(self.text_edit.redo)
        edit_menu.addAction(redo_act)

        cut_act = QAction(QIcon(self.getIconPath()), 'Cut', self)
        cut_act.setShortcut('Ctrl+X')
        cut_act.triggered.connect(self.text_edit.cut)
        edit_menu.addAction(cut_act)

        copy_act = QAction(QIcon(self.getIconPath()), 'Copy', self)
        copy_act.setShortcut('Ctrl+C')
        copy_act.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_act)

        paste_act = QAction(QIcon(self.getIconPath()), 'Paste', self)
        paste_act.setShortcut('Ctrl+V')
        paste_act.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_act)

        find_act = QAction(QIcon(self.getIconPath()), 'Find', self)
        find_act.setShortcut('Ctrl+F')
        find_act.triggered.connect(self.findText)
        edit_menu.addAction(find_act)

        # Tools menu
        tools_menu = menu_bar.addMenu('Tools')

        font_act = QAction(QIcon(self.getIconPath()), 'Font', self)
        font_act.setShortcut('Ctrl+G')
        font_act.triggered.connect(self.changeFont)
        tools_menu.addAction(font_act)

        color_act = QAction(QIcon(self.getIconPath()), 'Color', self)
        color_act.setShortcut('Ctrl+J')
        color_act.triggered.connect(self.changeColor)
        tools_menu.addAction(color_act)

        highlight_act = QAction(QIcon(self.getIconPath()), 'Highlight', self)
        highlight_act.setShortcut('Ctrl+I')
        highlight_act.triggered.connect(self.highlightText)
        tools_menu.addAction(highlight_act)

        # Help menu
        help_menu = menu_bar.addMenu('Help')

        help_act = QAction(QIcon(self.getIconPath()), 'About', self)
        help_act.setShortcut('Ctrl+H')
        help_act.triggered.connect(self.showAbout)
        help_menu.addAction(help_act)

    def clearText(self):
        if self.text_edit.toPlainText() != '':
            ok = QMessageBox.question(self, 'Are you sure?',
                                      'You will lose all unsaved data!',
                                      QMessageBox.Ok | QMessageBox.Cancel)
            if ok == QMessageBox.Ok:
                self.text_edit.clear()

    def openNote(self):
        filename = QFileDialog.getOpenFileName(self, 'Open note', './notes/',
                                               "HTML Files (*.html);;Text Files (*.txt)")[0]
        if filename:
            try:
                with open(filename, 'r') as f:
                    text = f.read()
                    self.text_edit.setText(text)
            except Exception as e:
                print(e)

    def saveNote(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File',
                                                   "./notes/",
                                                   "HTML Files (*.html);;Text Files (*.txt)")
        print(file_name)
        if file_name.endswith('.txt'):
            notepad_text = self.text_edit.toPlainText()
            with open(file_name, 'w') as f:
                f.write(notepad_text)
        elif file_name.endswith('.html'):
            notepad_richtext = self.text_edit.toHtml()
            with open(file_name, 'w') as f:
                f.write(notepad_richtext)
        else:
            QMessageBox.information(self, "Error",
                                    "Unable to save file.", QMessageBox.Ok)

    def findText(self):
        find_text, ok = QInputDialog.getText(self, "Search Text", "Find:")

        extra_selections = []

        if find_text and ok and not self.text_edit.isReadOnly():
            self.text_edit.moveCursor(QTextCursor.Start)
            color = QColor(Qt.yellow)
            while self.text_edit.find(find_text):
                selection = self.text_edit.ExtraSelection()
                selection.format.setBackground(color)
                selection.cursor = self.text_edit.textCursor()
                extra_selections.append(selection)
            self.text_edit.setExtraSelections(extra_selections)

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        self.text_edit.setCurrentFont(font)

    def changeColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)

    def highlightText(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextBackgroundColor(color)

    def showAbout(self):
        QMessageBox.about(self, 'About', 'Cool notepad which is developed for studying goals')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())