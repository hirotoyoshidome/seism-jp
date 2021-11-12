import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,100)
    w.setWindowTitle("テスト")
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
