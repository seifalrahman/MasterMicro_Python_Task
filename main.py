from HelperFunctions import drawUserFunctions
from PySide2.QtWidgets import QApplication
from GUIFunctions import Window, myApp
import matplotlib as plt
import sys

if __name__ == '__main__':

    window = Window()
    window.showFullScreen()
    myApp.exec_()
    sys.exit(0)
