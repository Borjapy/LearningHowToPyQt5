# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:53:41 2022

@author: borja

Creating first layout.
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys 

class Color(QWidget):
    def __init__(self, color, *args, **kargs):
        super(Color, self).__init__(*args, **kargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        
        
        
        
class MainWindow(QMainWindow):
    
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        self.setWindowTitle("My Awesome App")
        
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        #      margin order:    left top right bottom
        layout1.setContentsMargins( 5, 10, 15, 20 )
        
        layout2.setSpacing(20)
        
        layout2.addWidget( Color('red'))
        layout2.addWidget( Color('yellow'))
        layout2.addWidget( Color('purple'))
        

        layout3.addWidget( Color('red'))
        layout3.addWidget( Color('purple'))
        
        layout1.addLayout( layout2 )
        
        layout1.addWidget(Color('red'))
        layout1.addWidget(Color('green'))
        layout1.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout1)

        layout1.addLayout( layout3 )
        
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()