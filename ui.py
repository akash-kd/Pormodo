import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication as App
from PyQt5.QtWidgets import QHBoxLayout as HoriArr
from PyQt5.QtWidgets import QVBoxLayout as VertArr
from PyQt5.QtWidgets import QLabel as Label
from PyQt5.QtWidgets import QWidget as Widg
from PyQt5.QtWidgets import QPushButton as Pbutton
from PyQt5 import QtGui

Primaryfont = QtGui.QFont('Jetbrains Mono',12,QtGui.QFont.ExtraBold)
Secondaryfont = QtGui.QFont('Jetbrains Mono',14,QtGui.QFont.Medium)


class MainWindow(Widg):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.label = Label("Hello")

app = App([])
mw = MainWindow()
mw.show()
sys.exit(app.exec_())