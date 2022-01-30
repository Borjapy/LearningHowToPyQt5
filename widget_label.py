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
        
        
        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont( font )
        widget.setLayout(layout)
        
        widget.setAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
        
        self.setCentralWidget(widget)
        
        # We can introduce images with qlabel
        # Warning! this overshow the previous widget
        widgetImage = QLabel()
        widgetImage.setPixmap( QPixmap("sample_image.jpg") )
        widgetImage.setScaledContents( True )
        widgetImage.setLayout(layout)
        self.setCentralWidget(widgetImage)
        
        
        

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()