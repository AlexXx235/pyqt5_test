import sys
import os
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QDockWidget, QToolBar,
                             QLabel, QStatusBar, QTextEdit, QDesktopWidget, QFileDialog, QSizePolicy,
                             QMessageBox, QWidget, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap, QTransform, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class PhotoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setFixedSize(650, 650)
        self.setWindowTitle('Photo Editor')
        self.centerMainWindow()
        self.createImageWidgets()
        self.createDockWidget()
        self.createMenu()
        self.createToolBar()
        self.createStatusBar()
        self.show()

    def createImageWidgets(self):
        self.image = QPixmap()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)

        self.setCentralWidget(self.image_label)

    def getIconPath(self):
        return './images/icons/' + random.choice(os.listdir('./images/icons/'))

    def centerMainWindow(self):
        # Get screen W and H
        desktop = QDesktopWidget().screenGeometry()
        screen_width = desktop.width()
        screen_height = desktop.height()

        # Move to center
        self.move(int((screen_width - self.width()) / 2),
                  int((screen_height - self.height()) / 2))

    def createMenu(self):
        # Create menu bar
        menu_bar = self.menuBar()

        # Create menus
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        view_menu = menu_bar.addMenu('View')

        # File menu actions
        self.open_act = QAction(QIcon(self.getIconPath()), 'Open', self)
        self.open_act.setShortcut('Ctrl+O')
        self.open_act.setStatusTip('Open another image')
        self.open_act.triggered.connect(self.openImage)

        self.save_act = QAction(QIcon(self.getIconPath()), 'Save', self)
        self.save_act.setShortcut('Ctrl+S')
        self.save_act.setStatusTip('Save changed image')
        self.save_act.triggered.connect(self.saveImage)

        self.print_act = QAction(QIcon(self.getIconPath()), 'Print', self)
        self.print_act.setShortcut('Ctrl+P')
        self.print_act.setStatusTip('Print image')
        self.print_act.setEnabled(False)
        self.print_act.triggered.connect(self.printImage)

        self.exit_act = QAction(QIcon(self.getIconPath()), 'Exit', self)
        self.exit_act.setShortcut('Ctrl+Q')
        self.exit_act.setStatusTip('Quit program')
        self.exit_act.triggered.connect(self.close)

        # Add actions to file_menu
        file_menu.addAction(self.open_act)
        file_menu.addAction(self.save_act)
        file_menu.addAction(self.print_act)
        file_menu.addAction(self.exit_act)

        # Edit menu actions
        flip_act = QAction(QIcon(self.getIconPath()), 'Flip', self)
        flip_act.setShortcut('Ctrl+F')
        flip_act.setStatusTip('Flip image')
        flip_act.triggered.connect(self.flipImageVertical)

        resize_act = QAction(QIcon(self.getIconPath()), 'Resize', self)
        resize_act.setShortcut('Ctrl+R')
        resize_act.setStatusTip('Resize image')
        resize_act.triggered.connect(self.resizeImageHalf)

        clear_image_act = QAction(QIcon(self.getIconPath()), 'Clear Image', self)
        clear_image_act.setShortcut('Ctrl+C')
        clear_image_act.setStatusTip('Clear image')
        clear_image_act.triggered.connect(self.clearImage)

        # Add actions to edit menu
        edit_menu.addAction(flip_act)
        edit_menu.addAction(resize_act)
        edit_menu.addAction(clear_image_act)

        # Add actions to view menu
        view_menu.addAction(self.tools_show_act)

    def createToolBar(self):
        # Create toolbar and actions
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(50, 50))
        toolbar.addAction(self.open_act)
        toolbar.addAction(self.save_act)
        toolbar.addAction(self.print_act)
        toolbar.addAction(self.exit_act)

        # Add toolbar to main window
        self.addToolBar(toolbar)

    def createDockWidget(self):
        # Create dock widget
        self.dock_widget = QDockWidget('Edit image tools', self)
        self.dock_widget.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)
        self.dock_widget.setWidget(QTextEdit())

        # Create widget containing buttons
        self.dock_content = QWidget()

        # Image edit buttons
        self.rotate90 = QPushButton('Rotate 90')
        self.rotate90.setMinimumSize(QSize(130, 40))
        self.rotate90.setStatusTip('Rotate image 90 clockwise')
        self.rotate90.clicked.connect(self.rotateImage90)

        self.rotate180 = QPushButton('Rotate 180')
        self.rotate180.setMinimumSize(QSize(130, 40))
        self.rotate180.setStatusTip('Rotate image 180 clockwise')
        self.rotate180.clicked.connect(self.rotateImage180)

        self.flip_horizontal = QPushButton('Flip Horizontal')
        self.flip_horizontal.setMinimumSize(QSize(130, 40))
        self.flip_horizontal.setStatusTip('Flip image across horizontal axis')
        self.flip_horizontal.clicked.connect(self.flipImageHorizontal)

        self.flip_vertical = QPushButton("Flip Vertical")
        self.flip_vertical.setMinimumSize(QSize(130, 40))
        self.flip_vertical.setStatusTip('Flip image across vertical axis')
        self.flip_vertical.clicked.connect(self.flipImageVertical)

        self.resize_half = QPushButton("Resize Half")
        self.resize_half.setMinimumSize(QSize(130, 40))
        self.resize_half.setStatusTip('Resize image to half the original size')
        self.resize_half.clicked.connect(self.resizeImageHalf)

        # Put button to vertical layout
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(self.rotate90)
        dock_v_box.addWidget(self.rotate180)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.flip_horizontal)
        dock_v_box.addWidget(self.flip_vertical)
        dock_v_box.addStretch(1)
        dock_v_box.addWidget(self.resize_half)
        dock_v_box.addStretch(6)

        # Layout dock content and add to dock
        self.dock_content.setLayout(dock_v_box)
        self.dock_widget.setWidget(self.dock_content)

        # Add dock to main window
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)

        # Handles the visibility of the dock widget
        self.tools_show_act = self.dock_widget.toggleViewAction()

        # Add dock widget to main window
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)


    def createStatusBar(self):
        self.setStatusBar(QStatusBar())

    def openImage(self):
        image_file, _ = QFileDialog.getOpenFileName(self, 'Select image', './images/icons/',
                                                 'PNG (*.png)')
        if image_file:
            try:
                self.image = QPixmap(image_file)
                self.image_label.setPixmap(self.image.scaled(self.image_label.size(),
                                           Qt.KeepAspectRatio, Qt.SmoothTransformation))
            except Exception as e:
                print(e)

        else:
            QMessageBox.information(self, "Error",
                                    "Unable to open image.", QMessageBox.Ok)
        self.print_act.setEnabled(True)

    def saveImage(self):
        image_file, _ = QFileDialog.getSaveFileName(self, "Save Image", "./images/",
                                                    "PNG (*.png)")
        if image_file and self.image.isNull() is False:
            self.image.save(image_file)
        else:
            QMessageBox.information(self, "Error",
                                    "Unable to save image.", QMessageBox.Ok)

    def printImage(self):
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.NativeFormat)

        print_dialog = QPrintDialog(printer)
        if print_dialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter()
            painter.begin(printer)
            rect = QRect(painter.viewport())
            size = self.image_label.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image_label.pixmap().rect())
            # Scale the image_label to fit the rect source (0, 0)
            painter.drawPixmap(0, 0, self.image_label.pixmap())
            # End painting
            painter.end()

    def clearImage(self):
        self.image_label.clear()
        self.image = QPixmap()

    def rotateImage90(self):
        if not self.image.isNull():
            transform90 = QTransform().rotate(90)
            pixmap = QPixmap(self.image)
            rotated = pixmap.transformed(transform90, mode=Qt.SmoothTransformation)
            self.image_label.setPixmap(rotated.scaled(self.image_label.size(),
                                                      Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(rotated)
            self.image_label.repaint()  # repaint the child widget

    def rotateImage180(self):
        if not self.image.isNull():
            rotate180 = QTransform().rotate(180)
            pixmap = QPixmap(self.image)
            rotated = pixmap.transformed(rotate180, mode=Qt.SmoothTransformation)
            self.image_label.setPixmap(rotated.scaled(self.image_label.size(), Qt.KeepAspectRatio,
                                                      Qt.SmoothTransformation))
            self.image = rotated
            self.image_label.repaint()

    def flipImageVertical(self):
        if self.image.isNull() == False:
            flip_v = QTransform().scale(-1, 1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_v)
            self.image_label.setPixmap(flipped.scaled(self.image_label.size(),
                                                      Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.image_label.repaint()

    def flipImageHorizontal(self):
        if self.image.isNull() == False:
            flip_h = QTransform().scale(1, -1)
            pixmap = QPixmap(self.image)
            flipped = pixmap.transformed(flip_h)
            self.image_label.setPixmap(flipped.scaled(self.image_label.size(),
                                                      Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(flipped)
            self.image_label.repaint()

    def resizeImageHalf(self):
        if self.image.isNull() == False:
            resize = QTransform().scale(0.5, 0.5)
            pixmap = QPixmap(self.image)
            resized = pixmap.transformed(resize)
            self.image_label.setPixmap(resized.scaled(self.image_label.size(),
                                                      Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.image = QPixmap(resized)
            self.image_label.repaint()

    def changeDockWidgetState(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontShowIconsInMenus, True)
    window = PhotoEditor()
    sys.exit(app.exec_())