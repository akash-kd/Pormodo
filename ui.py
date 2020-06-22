import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication as App
from PyQt5.QtWidgets import QHBoxLayout as HoriArr
from PyQt5.QtWidgets import QVBoxLayout as VertArr
from PyQt5.QtWidgets import QLabel as Label
from PyQt5.QtWidgets import QWidget as Widg
from PyQt5.QtWidgets import QPushButton as Pbutton
from PyQt5.QtWidgets import QSlider as Slider
from PyQt5.QtWidgets import QDial as Dial

from PyQt5 import QtGui

Primaryfont = QtGui.QFont('Jetbrains Mono',12,QtGui.QFont.Bold)
Secondaryfont = QtGui.QFont('Jetbrains Mono',10,QtGui.QFont.Medium)
SliderFont = QtGui.QFont('Jetbrains Mono',90,QtGui.QFont.Bold)
Workmins = 25



class MainWindow(Widg):
    def __init__(self):
        super(MainWindow,self).__init__()
        #component
        self.layout = VertArr()
        self.dial = Dial()

        #layout setting
        self.layout.addWidget(TitleBar(self))
        self.layout.addWidget(Main(self))
        self.layout.addStretch(0)
        self.layout.setContentsMargins(0,0,0,0)

        #self setting
        self.setLayout(self.layout)
        self.setMaximumHeight(400)
        self.setMaximumWidth(400)
        self.setMinimumHeight(400)
        self.setMinimumWidth(400)
        self.setWindowFlag(Qt.FramelessWindowHint)






class TitleBar(Widg):
    def __init__(self,parent):
        super(TitleBar,self).__init__(parent)
        #component
        self.label = Label("PORMODO")
        self.closeButton = Pbutton()
        self.layout = HoriArr()
    
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
        self.closeButton.installEventFilter(self)
        #self setting
        self.setLayout(self.layout)

    def closeButtonClicked(self):
        app.exit()
    
    def eventFilter(self,obj,event):
        if obj == self.closeButton and event.type() == QtCore.QEvent.HoverEnter:
            self.closeButton.setStyleSheet("""
                                        background-image:url(closeHovered.png);
                                        height:30px;
                                        width:30px;
                                        border:none;
                                        """)
        if obj == self.closeButton and event.type() == QtCore.QEvent.HoverLeave:
                    self.closeButton.setStyleSheet("""
                                    background-image:url(close.png);
                                    height:30px;
                                    width:30px;
                                    border:none;
                                    """)
        return super(TitleBar, self).eventFilter(obj, event)


class Main(Widg):
    def __init__(self,parent):
        super(Main,self).__init__(parent)
        #components
        self.Vlayout = VertArr()
        #vlayout setting
        self.Vlayout.addWidget(SubMain(self))
        self.Vlayout.addWidget(Play(self))
        self.Vlayout.setAlignment(Qt.AlignCenter)
        #self setting
        self.setLayout(self.Vlayout)

    

class SubMain(Widg):
    testing = "something"
    def __init__(self,parent):
        super(SubMain,self).__init__(parent)
        #component
        self.Hlayout = HoriArr()
        self.label = Label("hello")
        #hlayout setting
        self.Hlayout.addWidget(WorkSlider(self))
        self.Hlayout.addWidget(BreakSlider(self))
        self.Hlayout.setContentsMargins(0,0,0,0)
        self.Hlayout.setAlignment(Qt.AlignCenter)
        # self setting
        self.setLayout(self.Hlayout)
        print(self.label.text())

    def setWorkMins(self,val):
        self.workMins = val
        print(self.workMins)
        
        


class WorkSlider(Widg):
    mins = 25
    def __init__(self,parent):
        super(WorkSlider,self).__init__(parent)
        #components
        self.layout = VertArr()
        self.slider = Slider()
        self.label = Label('25')
        #label Setting
        self.label.setFont(SliderFont)
        self.label.setAlignment(Qt.AlignCenter)
        
        #slider setting
        self.slider.setRange(0,60)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(Slider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.sliderValuedChanged)
        self.slider.setFixedWidth(150)
        self.slider.setValue(25)
        

        #self.layout setting
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.layout.setAlignment(Qt.AlignCenter)

        #self setting
        self.setLayout(self.layout)
    def sliderValuedChanged(self):
        print(self.slider.value())
        Workmins = self.slider.value()
        self.label.setText(str(self.slider.value()))
        print(Workmins)
        self.parent().setWorkMins(self.slider.value())
        




class BreakSlider(Widg):
    mins = 5
    def __init__(self,parent):
        super(BreakSlider,self).__init__(parent)
        #components
        self.layout = VertArr()
        self.slider = Slider()
        self.label = Label('5')
        

        #label Setting
        self.label.setFont(SliderFont)
        self.label.setAlignment(Qt.AlignCenter)
        
        #slider setting
        self.slider.setRange(0,60)
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(Slider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.sliderValuedChanged)
        self.slider.setFixedWidth(150)
        self.slider.setValue(5)
        

        #self.layout setting
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.slider)
        self.layout.setAlignment(Qt.AlignCenter)

        #self setting
        self.setLayout(self.layout)

        #self variable 

    def sliderValuedChanged(self):
        print(self.slider.value())
        self.label.setText(str(self.slider.value()))


    


class Play(Widg):
    def __init__(self,parent):
        super(Play,self).__init__(parent)
        #component
        self.layout = HoriArr()
        self.label = Label('heh')
        self.playButton = Pbutton('Start')
        self.pauseButton = Pbutton('Pause')
        self.WorkMins = 25
        self.BreakMins = 25

        #layout setting
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.playButton)
        self.layout.addWidget(self.pauseButton)
        
        #playbutton Setting
        self.playButton.setFont(Secondaryfont)
        self.playButton.clicked.connect(self.SetText)

        #pauseButton setting
        self.pauseButton.setFont(Secondaryfont)

        #self setting
        self.setLayout(self.layout)

    def SetText(self):
        self.label.setText(str(Workmins))



        


        




app = App([])
mw = MainWindow()
mw.show()
sys.exit(app.exec_())