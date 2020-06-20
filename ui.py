import sys

from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication as App
from PyQt5.QtWidgets import QHBoxLayout as HoriArr
from PyQt5.QtWidgets import QVBoxLayout as VertArr
from PyQt5.QtWidgets import QLabel as Label
from PyQt5.QtWidgets import QWidget as Widg
from PyQt5.QtWidgets import QPushButton as Pbutton
from PyQt5.QtWidgets import QDial as Dial
from PyQt5 import QtGui

Primaryfont = QtGui.QFont('Jetbrains Mono',12,QtGui.QFont.Bold)
Secondaryfont = QtGui.QFont('Jetbrains Mono',14,QtGui.QFont.Medium)



class MainWindow(Widg):
    def __init__(self):
        super(MainWindow,self).__init__()
        #component
        self.layout = VertArr()
        self.dial = Dial()

        #layout setting
        self.layout.addWidget(TitleBar(self))
        self.layout.addWidget(self.dial)
        self.layout.addStretch(0)
        self.layout.setContentsMargins(0,0,0,0)

        #dial setting
        self.dial.setFixedHeight(300)
        #self setting
        self.setLayout(self.layout)
        self.setMaximumHeight(400)
        self.setMaximumWidth(400)
        self.setMinimumHeight(400)
        self.setMinimumWidth(400)
        self.setWindowFlag(Qt.FramelessWindowHint)
        



class TitleBar(Widg):
    def __init__(self,parent):
        super(TitleBar,self).__init__()
        #component
        self.label = Label("Hello")
        self.layout = HoriArr()
        self.closeButton = Pbutton()
    

        #layout setting
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.closeButton)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setAlignment(Qt.AlignTop)
        #label setting
        self.label.setStyleSheet("""background-color:#6DF2A7;""")
        self.label.setFixedHeight(30)
        self.label.setFixedWidth(400)
        self.label.setFont(Primaryfont)
        self.label.setAlignment(Qt.AlignCenter)
        #close button setting
        self.closeButton.setStyleSheet("""
                                    background-image:url(close.png);
                                    height:30px;
                                    width:30px;
                                    border:none;
                                    """)
        self.closeButton.clicked.connect(self.closeButtonClicked)
        #self setting
        self.setLayout(self.layout)

    def closeButtonClicked(self):
        app.exit()



app = App([])
mw = MainWindow()
mw.show()
sys.exit(app.exec_())