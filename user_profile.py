import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QFont


class UserProfileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 500)
        self.setWindowTitle("Alex's profile")
        self.display_images()
        self.display_text()
        self.show()

    def display_images(self):
        background_image = "images/background.jpg"
        profile_image = "images/alex.jpg"

        try:
            with open(background_image):
                back_label = QLabel(self)
                back_label.setGeometry(0, 0, 400, 100)
                pixmap = QPixmap(background_image).scaled(400, 100)
                back_label.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found")

        try:
            with open(profile_image):
                profile_label = QLabel(self)
                profile_label.setGeometry(150, 0, 100, 100)
                pixmap = QPixmap(profile_image).scaled(100, 100)
                profile_label.setPixmap(pixmap)
        except FileNotFoundError:
            print("Image not found")

    def display_text(self):
        name_label = QLabel(self)
        name_label.setGeometry(175, 100, 100, 50)
        name_label.setText("Alex")
        name_label.setFont(QFont('Arial', 20))

        bio_title_label = QLabel(self)
        bio_title_label.setGeometry(0, 150, 125, 50)
        bio_title_label.setText("Biography")
        bio_title_label.setFont(QFont('Arial', 17))

        about_label = QLabel(self)
        about_label.setGeometry(0, 200, 400, 200)
        about_label.setText("I am a very tired student who has to do data management course work. "
                            "But i really enjoy this since i can select using technologies by myself"
                            " and also i actually have a lof of time so... It's nice.")
        about_label.setFont(QFont('Arial', 12))
        about_label.setWordWrap(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserProfileWindow()
    sys.exit(app.exec_())
