import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QMenuBar, QToolBar, QStyle
from PyQt6.QtGui import QIcon, QAction, QKeySequence

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('New Title For Our Window')
        self.setGeometry(100, 100, 500, 300)
        #self.showMaximized()    

        action1 = QAction('Exit', self)
        action1.triggered.connect(self.close)
        self.menuBar().addAction(action1)


def main():
    app = QApplication(sys.argv)
    
    main_win = MainWindow()
    main_win.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing PyQt6 Main Window...')   


if __name__ == "__main__":
    main()