# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 11:13:42 2022

@author: Borja Garcia

Toolbars and Actions

"""


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys 

class MainWindow(QMainWindow):
    
    def __init__( self, *args, **kargs):
        super(MainWindow, self).__init__(*args, **kargs)
        
        self.setWindowTitle("My Awesome App")
        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(50, 16))
        
        #toolbar.ToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # Pendiente investigar lo de los estilos de texto/iconos
        
        self.addToolBar(toolbar)
        
        # Primer boton
        button_action = QAction(QIcon("bug--plus.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        
        # Segundo boton
        button_action2 = QAction(QIcon("bug--plus.png"), u"Your &button", self)
        button_action2.setStatusTip("This is your button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        
        # Checkbox con su etiqueta
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())
        
        self.setStatusBar(QStatusBar(self))
        
        # Creando un menu
        menu = self.menuBar()
        menu.setNativeMenuBar(False) #Disables the global menu baar on MacOS
        
        file_menu = menu.addMenu(u"&File")
        file_menu.addAction(button_action)
        
        file_menu.addSeparator()
        
        file_menu = file_menu.addMenu("Submenu")
        
        file_menu.addAction(button_action2)
        
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show() # IMPORTANT!!

app.exec_()


