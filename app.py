import os
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QMenuBar, QToolBar, QStyle
from PyQt6.QtGui import QIcon, QAction

ICONS_PATH = 'images/'      # Copy your toolbar icons in this folder
WIN_X = 100                 # Top position of main window
WIN_Y = 100                 # Left position of main window
WIN_W = 500                 # Main window width by default
WIN_H = 300                 # Main window height by default

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Editor')
        self.setGeometry(WIN_X, WIN_Y, WIN_W, WIN_H)
        #self.showMaximized()

        self._define_actions()
        self._create_top_menu()
        self._create_tool_bar()

        self.central_widget = CentralWidget()
        self.setCentralWidget(self.central_widget)

    def _define_actions(self):
        '''
        Qt seems to have a problem when setting ShowIconsInMenu to False. If an Icon is added to an action it will be displayed in the menu.
        To work around this create two actions (use _icon for the toolbar icons), but connect the same method on triggered.
        '''
        
        self.action_exit = QAction('&Exit')
        self.action_exit.triggered.connect(self.do_shut_down)

        about_icon = QIcon(os.path.join(ICONS_PATH, 'information.png' ))
        self.action_about = QAction('&About')
        self.action_about_icon = QAction(about_icon, '&About')
        self.action_about.setIconVisibleInMenu(False)       
        self.action_about.triggered.connect(self.do_print_about)
        self.action_about_icon.triggered.connect(self.do_print_about)
        
        db_icon = QIcon(os.path.join(ICONS_PATH, 'database--arrow.png' ))
        self.action_opendb = QAction('&Open DB')
        self.action_opendb_icon = QAction(db_icon, "&Open DB")
        self.action_opendb.triggered.connect(self.do_connect_db)
        self.action_opendb_icon.triggered.connect(self.do_connect_db)


    def _create_top_menu(self):
        top_menu = self.menuBar()                       

        # File menu and its actions in submenus
        file_menu = top_menu.addMenu("&File")           
        file_menu.addAction(self.action_opendb)
        file_menu.addSeparator()
        file_menu.addAction(self.action_exit)
        top_menu.addMenu(file_menu)
        
        # About action on top menu
        top_menu.addAction(self.action_about)

    def _create_tool_bar(self):
        tool_bar = QToolBar()
        tool_bar.addAction(self.action_opendb_icon)
        tool_bar.addAction(self.action_about_icon)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

    def do_connect_db(self):
        print('Connecting to database')

    def do_print_about(self):
        print('Show about window popup')
        
    def do_shut_down(self):
        self.close()

class CentralWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create and attach a layout to the widget
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create components and add them to the Layout
        label = QLabel("Central Widget with a simple label")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

def main():
    app = QApplication(sys.argv)
    
    app.setDesktopSettingsAware(False)
    app.setAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus, on=False)

    main_window = MainWindow()
    main_window.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing PyQt6 Main Window...')    

if __name__ == "__main__":
    main()

    #EXTRA CODE TO LOOK AT, REMOVE THIS SECTION
    #print(f'ShowIconsInMenu: {app.testAttribute(Qt.ApplicationAttribute.AA_DontShowIconsInMenus)}')
    #print(f'AboutQt: {app.aboutQt()}')
    #app.beep()
    #print(f'Application Style Object: {app.style}')
    # icons = sorted([attr for attr in dir(QStyle.StandardPixmap) if attr.startswith("SP_")])
    # for icon in icons:
    #     print(icon)    
