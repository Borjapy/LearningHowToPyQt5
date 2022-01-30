# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:53:41 2022

@author: borja

Creating first PyQt5 window.
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import sys 
import os 

class MainWindow(QMainWindow):
    
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        self.setWindowTitle("My Awesome App")
        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)
        
        file_menu = self.menuBar().addMenu("&File")
        
        # This action allows to open a file with the program
        print_action = QAction( QIcon(), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect( self.print_page )
        file_menu.addAction( print_action )
        
        self.setCentralWidget(label)

    # This function reads a html file and opens it if as browser if it is a html file
    def print_page(self):
        dlg = QPrintPreviewDialog()
        #dlg.paintRequested( -- this goes the document to print -- )
        dlg.exec_()
        print("PRINTING!!")            

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()