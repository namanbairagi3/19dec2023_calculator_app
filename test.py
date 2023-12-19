#import area
import sys
#from topmodule.submodule import elim1,elim2,elim3,...
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QIcon

#create class object
app = QApplication(sys.argv) 

window = QMainWindow()
window.setWindowTitle("Abhishek Calculator")  # Set the window title
window.showMaximized()

iconCO = QIcon('./Calculator.png') #set the window icon
window.setWindowIcon(iconCO)

#create a menu bar
menubar = window.menuBar()
file_menu =menubar.addMenu("Programmer") # set the menu

#file_menu =menubar.addMenu("Converter")  # set the menu
#file_menu =menubar.addMenu("Settings")  # set the menu


app.exec()