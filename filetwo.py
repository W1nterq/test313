from PyQt5.QtWidgets import QApplication
from first import First
from second import Second

app = QApplication([])
win1 = First()
win2 = Second()
app.exec()