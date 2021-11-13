import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QPushButton, QLabel

app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()
width = screen.size().width()
height = screen.size().height()


class Sample(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setGeometry(0, 0, width, height)
        self.setWindowTitle("Sample")
        self.initUI()

    def initUI(self):
        self.main_widget = QWidget()
        self.grid = QGridLayout()
        self.main_widget.setLayout(self.grid)
        self.setCentralWidget(self.main_widget)

        self.description = QLabel()
        self.description.setText("page.")

        self.grid.addWidget(self.description, 0, 0)
