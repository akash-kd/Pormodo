import sys
import time

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QApplication as App
from PyQt5.QtWidgets import QDial as Dial
from PyQt5.QtWidgets import QHBoxLayout as HoriArr
from PyQt5.QtWidgets import QLabel as Label
from PyQt5.QtWidgets import QPushButton as Pbutton
from PyQt5.QtWidgets import QSlider as Slider
from PyQt5.QtWidgets import QVBoxLayout as VertArr
from PyQt5.QtWidgets import QWidget as Widg

Primaryfont = QtGui.QFont('Jetbrains Mono',12,QtGui.QFont.Bold)
Secondaryfont = QtGui.QFont('Jetbrains Mono',10,QtGui.QFont.Medium)
SliderFont = QtGui.QFont('Jetbrains Mono',90,QtGui.QFont.Bold)

class MainWindow(Widg):
    def __init__(self):
        super(MainWindow,self).__init__()
        #component
        self.layout = VertArr()
        #title Bar component
        self.TitleBarlabel = Label("PORMODO")
        self.TitleBarlayout = HoriArr()
        self.TitleBarcloseButton = Pbutton()
        #TitleBar layout settinh
        self.TitleBarlayout.addWidget(self.TitleBarlabel)
        self.TitleBarlayout.addWidget(self.TitleBarcloseButton)
        self.TitleBarlayout.setContentsMargins(0,0,0,0)
        self.TitleBarlayout.setAlignment(Qt.AlignTop)
        #Title Bar label setting
        self.TitleBarlabel.setStyleSheet("""background-color:#6DF2A7;""")
        self.TitleBarlabel.setFixedHeight(30)
        self.TitleBarlabel.setFixedWidth(400)
        self.TitleBarlabel.setFont(Primaryfont)
        self.TitleBarlabel.setAlignment(Qt.AlignCenter)
        #Title bar close button setting
        self.TitleBarcloseButton.setStyleSheet("""
                                    background-image:url(close.png);
                                    height:30px;
                                    width:30px;
                                    border:none;
                                    """)
        self.TitleBarcloseButton.clicked.connect(self.closeButtonClicked)
        self.TitleBarcloseButton.installEventFilter(self)


        #layout setting
        self.layout.addLayout(self.TitleBarlayout)
        self.layout.setContentsMargins(0,0,0,0)


        #self setting
        self.setLayout(self.layout)
        self.setMaximumHeight(400)
        self.setMaximumWidth(400)
        self.setMinimumHeight(400)
        self.setMinimumWidth(400)
        self.setWindowFlag(Qt.FramelessWindowHint)

        #Main components
        self.MainVlayout = VertArr()
        #MainVlayout setting
        self.MainVlayout.addLayout(SubMainHlayout(self))
        self.MainVlayout.addLayout(Play(self))
        self.MainVlayout.setAlignment(Qt.AlignCenter)

        #Submain component
        self.SubMainHlayout = HoriArr()
        #SubMainHlayout setting
        self.SubMainHlayout.addWidget(WorkSlider(self))
        self.SubMainHlayout.addWidget(BreakSlider(self))
        self.SubMainHlayout.setContentsMargins(0,0,0,0)
        self.SubMainHlayout.setAlignment(Qt.AlignCenter)
    
        



    def eventFilter(self,obj,event):
        if obj == self.TitleBarcloseButton and event.type() == QtCore.QEvent.HoverEnter:
            self.TitleBarcloseButton.setStyleSheet("""
                                        background-image:url(closeHovered.png);
                                        height:30px;
                                        width:30px;
                                        border:none;
                                        """)
        if obj == self.TitleBarcloseButton and event.type() == QtCore.QEvent.HoverLeave:
                    self.TitleBarcloseButton.setStyleSheet("""
                                    background-image:url(close.png);
                                    height:30px;
                                    width:30px;
                                    border:none;
                                    """)
        return super(MainWindow, self).eventFilter(obj, event)


    def closeButtonClicked(self):
        app.exit()




app = App([])
mw = MainWindow()
mw.show()
sys.exit(app.exec_())
