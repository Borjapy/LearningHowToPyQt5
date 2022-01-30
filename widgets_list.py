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
        
        
        widgets = [QCheckBox,
                  QComboBox,
                  QDateEdit,
                  QDateTimeEdit,
                  QDial,
                  QDoubleSpinBox,
                  QFontComboBox,
                  QLCDNumber,
                  QLabel,
                  QLineEdit,
                  QProgressBar,
                  QPushButton,
                  QRadioButton,
                  QSlider,
                  QSpinBox,
                  QTimeEdit]
        
        for w in widgets:
            layout.addWidget(w())
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()