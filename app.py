import sys
import os
import re
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout , QPushButton, QLabel

from layout_colorwidget import Color
from core import launch_DCC, Directory_folder




# Mengatur layout aplikasi
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Launcher")

        # initiate value for directory

        project_code = None

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()

        # Widget 1 #

        widget1 = Color("lightgrey")
        widget1.setMinimumSize(100,80)
        widget1.setMaximumSize(200,160)

        btn1 = QPushButton(widget1)
        btn1.setText('DRK')
        btn1.setFixedSize(200,160)
        
        

        # Widget 2 #

        widget2 = Color("lightgrey")
        widget2.setMinimumSize(100,80)
        widget2.setMaximumSize(200,160)

        btn2 = QPushButton(widget2)
        btn2.setText('SSM')
        btn2.setFixedSize(200,160)
        

        # Widget 3 #

        widget3 = Color("lightgrey")
        widget3.setMinimumSize(100,80)
        widget3.setMaximumSize(200,160)

        btn3 = QPushButton(widget3)
        btn3.setText('OPLA')
        btn3.setFixedSize(200,160)
        

        # Widget 4 #

        widget4 = Color("lightgrey")
        widget4.setMinimumSize(100,80)
        widget4.setMaximumSize(200,160)

        btn4 = QPushButton(widget4)
        btn4.setText('EFP2')
        btn4.setFixedSize(200,160)
        



        layout2.addWidget(widget1)
        layout2.addWidget(widget2)
        layout2.addWidget(widget3)
        layout2.addWidget(widget4)



        

        layout1.addLayout(layout2)

        widgetLauncher = Color("grey")
        Launcher_headLine = QLabel("        Launcher", widgetLauncher)
        # button for Katana
        DCC_btn1 = QPushButton(widgetLauncher)
        DCC_btn1.setText("Katana")
        DCC_btn1.setGeometry(10, 50, 100, 100)
        

        # button for nuke 
        DCC_btn2 = QPushButton(widgetLauncher)
        DCC_btn2.setText("Maya")
        DCC_btn2.setGeometry(130, 50, 100, 100)
        

        # button for nuke 
        DCC_btn3 = QPushButton(widgetLauncher)
        DCC_btn3.setText("Nuke")
        DCC_btn3.setGeometry(250, 50, 100, 100)
        
                

        # button for nuke 
        DCC_btn4 = QPushButton(widgetLauncher)
        DCC_btn4.setText("3dsMax")
        DCC_btn4.setGeometry(370, 50, 100, 100)
        









        layout1.addWidget(widgetLauncher)
    
        

        self.setMinimumSize(QSize(1000, 700))



        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)






app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()