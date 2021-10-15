import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFrame, QTextEdit, QPushButton,
                             QDockWidget, QVBoxLayout)
from PyQt5.QtCore import Qt


class ClipboardExample(QMainWindow):
    def __init__(self):
        super(ClipboardExample, self).__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Clipboard')
        self.setGeometry(100, 100, 600, 600)
        self.createMainWidget()
        self.createDockWidget()
        self.show()

    def createMainWidget(self):
        self.main_text_edit = QTextEdit()
        self.setCentralWidget(self.main_text_edit)

    def createDockWidget(self):
        clipboard_dock = QDockWidget('Clipboard Content')
        clipboard_dock.setAllowedAreas(Qt.TopDockWidgetArea)

        self.clipboard_text_edit = QTextEdit()
        paste_btn = QPushButton('Paste')
        paste_btn.clicked.connect(self.pasteText)

        main_v_box = QVBoxLayout()
        main_v_box.addWidget(self.clipboard_text_edit)
        main_v_box.addWidget(paste_btn)

        dock_frame = QFrame()
        dock_frame.setLayout(main_v_box)

        clipboard_dock.setWidget(dock_frame)
        self.addDockWidget(Qt.TopDockWidgetArea, clipboard_dock)

        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.copyFromClipboard)

    def pasteText(self):
        self.centralWidget().paste()

    def copyFromClipboard(self):
        mime_data = self.clipboard.mimeData()
        if mime_data.hasText():
            self.clipboard_text_edit.setText(mime_data.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClipboardExample()
    sys.exit(app.exec_())
