import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QMenuBar, QToolBar, QStyle
from PyQt6.QtGui import QIcon, QAction

def main():
    app = QApplication(sys.argv)
    
    main_win = QMainWindow()
    main_win.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing PyQt6 Main Window...')   


if __name__ == "__main__":
    main()
    