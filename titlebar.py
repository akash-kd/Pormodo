from gui import mw

#title Bar component
mw.TitleBarlabel = Label("PORMODO")
mw.TitleBarlayout = HoriArr()
mw.TitleBarcloseButton = Pbutton()
#TitleBar layout settinh
mw.TitleBarlayout.addWidget(mw.TitleBarlabel)
mw.TitleBarlayout.addWidget(mw.TitleBarcloseButton)
mw.TitleBarlayout.setContentsMargins(0,0,0,0)
mw.TitleBarlayout.setAlignment(Qt.AlignTop)
#Title Bar label setting
mw.TitleBarlabel.setStyleSheet("""background-color:#6DF2A7;""")
mw.TitleBarlabel.setFixedHeight(30)
mw.TitleBarlabel.setFixedWidth(400)
mw.TitleBarlabel.setFont(Primaryfont)
mw.TitleBarlabel.setAlignment(Qt.AlignCenter)
#Title bar close button setting
mw.TitleBarcloseButton.setStyleSheet("""
                            background-image:url(close.png);
                            height:30px;
                            width:30px;
                            border:none;
                            """)
