# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:53:41 2022

@author: borja

Creating a web browser.
This script does not work because deprecated methods

A nowadays version guide can be found: https://www.youtube.com/watch?v=KBLQ7GJLlQE

"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QWebKitWidgets import *

import sys 

class MainWindow(QMainWindow):
    
    # This script does not work because deprecated methods
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        self.show() 
        
        self.setWindowTitle("My Web Browser")
        self.setWindowIcon( QIcon(os.path.join('icons', 'file.png') ) )
        
        self.browser = QWebView()
        self.browser.setUrl( QUrl("http://www.google.com"))

        self.setCentralWidget(self.browser)

app = QApplication(sys.argv)

app.setApplicationName("Mozarella Ashbadger")
app.setOrganizationName("organization")
app.setOrganizationDomain("organization.org")

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()