# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:53:41 2022

@author: borja

Introducing detection of button signals
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys 

class MainWindow(QMainWindow):
    
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        
        self.setWindowTitle("My Awesome App")
        
        layout = QHBoxLayout()
        
        # Creo botones que al pulsarlos arrojaran un valor al programa
        for n in range(10):
            btn = QPushButton(str("boton " + str(n+1)))
            btn.pressed.connect( lambda n=n+1: self.my_custom_fn(n) )
            layout.addWidget(btn)
            
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
    def my_custom_fn(self, a):
        print(a)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()