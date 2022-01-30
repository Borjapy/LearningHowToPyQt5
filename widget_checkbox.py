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
        
        
        widget = QCheckBox()
        # Both following lines are equivalent
        widget.setChecked(True)
        widget.setCheckState(Qt.Checked)
        
        # It can be partially checked
        widget.setCheckState(Qt.PartiallyChecked)
        # This allows the partially checked
        widget.setTristate( True )
        
        # Next lines register state change in the checkbox
        widget.stateChanged.connect(self.show_state)
    
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.Checked )
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()