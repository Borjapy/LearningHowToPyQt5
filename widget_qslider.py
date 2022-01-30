# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:53:41 2022

@author: borja

Creating first PyQt5 window.
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys 

class MainWindow(QMainWindow):
    
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        self.setWindowTitle("My Awesome App")
        
        layout = QVBoxLayout()
        
        
        # Defining widget (allows double type numbers)
        widget = QSlider()
        
        # Widget Properties
        widget.setRange( -10, 3 )
        widget.setSingleStep( 1.1 )
        
        # Detecting signals
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        
        self.setCentralWidget(widget)

    def value_changed( self, i):
        print(i)

    def slider_position( self, i):
        print(i)

    def slider_pressed( self ):
        print("Pressed")
        
    def slider_released( self ):
        print("Released")

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()