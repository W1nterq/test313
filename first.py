from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from text import *

class First(QWidget):
    def __init__(self):
        super().__init__()
        self.show()

        self.setWindowTitle('Инструкция')
        label = QLabel(description)
        main_line = QVBoxLayout()
        main_line.addWidget(label)

        start_btn = QPushButton('Начать')
        main_line.addWidget(start_btn)

        self.setLayout(main_line)
        self.setStyleSheet('font-size:28px')

if __name__ == "__main__":
    app = QApplication([])
    win1 = First()
    app.exec()