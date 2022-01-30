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
import os 

class MainWindow(QMainWindow):
    
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        self.setWindowTitle("My Awesome App")
        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)
        
        file_menu = self.menuBar().addMenu("&File")
        
        # This action allows to open a file with the program
        open_file_action = QAction( QIcon( os.path.join('icon', 'disk--arrow.png')), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect( self.open_file )
        file_menu.addAction(open_file_action)
        
        save_file_action = QAction( QIcon( os.path.join('icon', 'disk--pencil.png')), "Save file...", self)
        save_file_action.setStatusTip("Save from file")
        save_file_action.triggered.connect( self.save_file )
        file_menu.addAction(save_file_action)
        
        
        self.setCentralWidget(label)

    # This function reads a html file and opens it if as browser if it is a html file
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName( self, "Open file", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files(*.*)")
        if filename: 
            with open(filename, 'r') as f:
                html = f.read()
            self.browser.setHtml( html )
        
    
    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName( self, "Save Page As", "",
                                                  "Hypertext Markup Language (*.htm *.html);;"
                                                  "All files(*.*)")
        if filename: 
            html = self.browser.page().mainFrame().toHtml()
            with open(filename, 'w') as f:
                f.write(html.encode('utf8'))
            

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()