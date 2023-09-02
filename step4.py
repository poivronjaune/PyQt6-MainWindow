import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QMenuBar, QToolBar, QStyle
from PyQt6.QtGui import QIcon, QAction

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('New Title For Our Window')
        self.setGeometry(100, 100, 500, 300)
        #self.showMaximized()

        self._define_actions()
        self._create_top_menu()

    def _define_actions(self):
        self.action1 = QAction('Menu One')
        self.action1.triggered.connect(self.do_action1)

    def _create_top_menu(self):
        top_menu = self.menuBar()   
        top_menu.addAction(self.action1)

    def do_action1(self):
        print('Menu One pressed...')

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