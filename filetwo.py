from PyQt5.QtWidgets import QApplication
from sfrhb import First
from filethree import Second

app = QApplication([])
win1 = First()
win2 = Second()
app.exec()