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
       
        tabs = QTabWidget()
        
        for n, color in enumerate(['red', 'green', 'blue', 'yellow']):
            tabs.addTab( Color( color ), color )
                    
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()