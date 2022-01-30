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
        
        
        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])
        widget.currentItemChanged.connect( self.item_changed )
        widget.currentTextChanged.connect( self.text_changed )
        self.setCentralWidget(widget)


    def item_changed( self, i):
        print(i.text(), i)

    def text_changed( self, s):
        print(s)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()