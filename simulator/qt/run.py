import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QPushButton, QLabel
from sample import Sample

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()
width = screen.size().width()
height = screen.size().height()


class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, width, height)
        self.setWindowTitle("Home")
        self.initUI()

    def click_button(self):
        # self.new_description = QLabel()
        # self.new_description.setText("Pushed!")
        # self.grid.addWidget(self.new_description, 0, 1)
        self.new = Sample(self)
        self.close()
        self.new.show()

    def initUI(self):
        self.main_widget = QWidget()
        self.grid = QGridLayout()
        self.main_widget.setLayout(self.grid)
        self.setCentralWidget(self.main_widget)

        # button
        self.button = QPushButton()
        self.button.setText("Push")
        self.button.setMaximumWidth(int(width / 7))
        self.button.setMaximumHeight(int(height / 10))
        self.button.clicked.connect(self.click_button)
        self.button.setStyleSheet("QPushButton::hover {background-color : lightblue;}")

        self.description = QLabel()
        self.description.setText("Push this button.")

        self.grid.addWidget(self.description, 0, 0)
        self.grid.addWidget(self.button, 0, 1)


def main():
    app = QApplication(sys.argv)
    win = StartWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
