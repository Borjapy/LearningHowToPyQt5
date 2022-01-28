# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:53:41 2022

@author: borja

Introducing detection of custom signals
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys 

class MainWindow(QMainWindow):
    
    my_awesome_signal = pyqtSignal(str)
    
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        # introduciendo lambda podemos evitar que coja el nombre del titulo como primer parametro
        # tambien podemos introducir la x en el lugar que queramos para controlarlo más
        #self.windowTitleChanged.connect( lambda x: self.my_custom_fn(x, 10) )
        
        self.setWindowTitle("My Awesome App")


        button = QPushButton("HELLO!")
        button.pressed.connect( self.pushed_my_button )
        
        self.my_awesome_signal.connect( self.caught_my_own_signal )
        self.setCentralWidget( button )

    def pushed_my_button(self):
        print("Pressed it!")        
        self.my_awesome_signal.emit("WOAH")
    
    def caught_my_own_signal(self, s):
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()