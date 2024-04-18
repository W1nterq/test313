from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from text import *

class First():
    def __init__(self):
        self.win = QWidget()
        self.win.show()

        self.win.setWindowTitle('Инструкция')
        label = QLabel(description)
        main_line = QVBoxLayout()
        main_line.addWidget(label)

        start_btn = QPushButton('Начать тест')
        main_line.addWidget(start_btn)

        self.win.setLayout(main_line)
        self.win.setStyleSheet('font-size:28px')

if __name__ == "__main__":
    app = QApplication([])
    win1 = First()
    app.exec()