import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QTextEdit, QFileDialog, QMessageBox


class NotepadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle("Notepad")
        self.diplayButtons()
        self.displayTextEdit()
        self.show()

    def diplayButtons(self):
        new_btn = QPushButton("new", self)
        save_btn = QPushButton("save", self)

        new_btn.setGeometry(30, 30, 80, 30)
        save_btn.setGeometry(130, 30, 80, 30)

        new_btn.clicked.connect(self.clearTextEdit)
        save_btn.clicked.connect(self.saveNote)

        new_btn.show()
        save_btn.show()

    def clearTextEdit(self):
        if self.text_edit.toPlainText() != '':
            answer = QMessageBox.question(self, 'Note is not empty!',
                                          "You have unsaved changes that will be lost. Continue?",
                                          QMessageBox.Cancel | QMessageBox.Ok)
            if answer == QMessageBox.Ok:
                self.text_edit.clear()

    def saveNote(self):
        note = self.text_edit.toPlainText()
        filename = QFileDialog.getSaveFileName(self, "Save note",
                                               os.getcwd(), "All Files (*);; Text Files (*.txt)")[0]
        if filename:
            with open(filename, 'w') as f:
                f.write(note)

    def displayTextEdit(self):
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(15, 80, 370, 400)
        self.text_edit.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NotepadWindow()
    sys.exit(app.exec_())
