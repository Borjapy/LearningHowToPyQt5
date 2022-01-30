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
        
        # Creating widget
        widget = QLineEdit()
        
        # Setting Properties:
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter your text")
        widget.setReadOnly(False)
        
        # Detecting widget singals:
        widget.returnPressed.connect(self.return_pressed) # This doesnt seems to work properly
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect( self.text_edited )
        
        self.setCentralWidget(widget)

    def return_pressed( self ):
        print("Return pressed!")
        self.centralWidget().selfText("BOOM")

    def selection_changed( self ):
        print("Selection changed")
        print( self.centralWidget().selectedText() )

    def text_changed( self, s):
        print("Text changed...")
        if( s == "DOGE" ):
            self.centralWidget().setText("No doges allowed.")
        else:
            print(s)
    
    def text_edited( self, s):
        print("Text edited...")
        print(s)
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()