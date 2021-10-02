import sys
import os
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QTextEdit, QToolBar,
                             QDockWidget, QStatusBar)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class ToolbarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 350, 350)
        self.setWindowTitle('Toolbar Window')
        self.setCentralWidget(QTextEdit())
        self.displayMenu()
        self.displayToolBar()
        self.createDockWidget()
        self.show()

    def getIconPath(self):
        return './images/icons/' + random.choice(os.listdir('./images/icons/'))

    def displayMenu(self):
        # Create menu bar
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu('File')

        # File menu actions
        self.exit_act = QAction(QIcon(self.getIconPath()), 'Exit', self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)

        file_menu.addAction(self.exit_act)

        # View menu
        view_menu = menu_bar.addMenu('View')

        # View submenu
        appearance_submenu = view_menu.addMenu('Appearance')

        # View's appearance submenu actions
        full_screen_act = QAction(QIcon(self.getIconPath()), 'Full screen', self, checkable=True)
        full_screen_act.setShortcut('Ctrl+F')
        full_screen_act.setStatusTip('Switch program view to Full Screen')
        full_screen_act.triggered.connect(self.setFullScreen)

        appearance_submenu.addAction(full_screen_act)

        self.setStatusBar(QStatusBar())

    def displayToolBar(self):
        toolbar = QToolBar('Main Toolbar')
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(toolbar)

        toolbar.addAction(self.exit_act)

    def createDockWidget(self):
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle('Example Dock')
        dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)

        dock_widget.setWidget(QTextEdit())

        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget)

    def setFullScreen(self, state):
        if state:
            self.showFullScreen()
        else:
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToolbarWindow()
    sys.exit(app.exec_())