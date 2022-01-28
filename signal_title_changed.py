# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:53:41 2022

@author: borja

Introducing detection of name app signal
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys 

class MainWindow(QMainWindow):
    
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        # introduciendo lambda podemos evitar que coja el nombre del titulo como primer parametro
        # tambien podemos introducir la x en el lugar que queramos para controlarlo más
        self.windowTitleChanged.connect( lambda x: self.my_custom_fn(x, 10) )
        
        self.setWindowTitle("My Awesome App")
        
        label = QLabel()
        label.setAlignment( Qt.AlignCenter )
        
        self.setCentralWidget(label)
        
    def onWindowTitleChange(self,s):
        print(s)
    def my_custom_fn(self, a="HELLO!!", b=5):
        print(a, b)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()