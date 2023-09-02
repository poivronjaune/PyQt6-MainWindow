# PyQt6 - Main Window Boiler Plate 
>**Warning**  
>This project provides no functionnality. It is only a PyQt6 Stub to start your own project. Many tutorials create a simple window using a QWidget that acts as the entry point of an app. We chose something else :)  

### We Hope this will help you get started
The basic Main Window Application can be found in the ***app.py*** script.

## Installation  

Clone this project on your windows environment and run  

> git clone git@github.com:poivronjaune/PyQt6-MainWindow.git  
> cd PyQt6-MainWindow  
>
> python -m venv env  
> .\env\Scripts\Activate  
> 
> python -m pip install --upgrade pip  
> pip install -e .  
>
> python app.py  

On linux use source bin/activate instead of .env\Scripts\Activate

## Basic usage  
For those who are familiar with python coding and packages, a PyQt6 Main Window application requires the following to be done:  
- Create a QApplication with the event loop that manages events, widgets and user interaction  
- Create a QMainWindow object on which to add other components  
- Create QActions with icons, text and connect callback methods to each  
- Attach a menuBar() to the QMainWindow and addActions() to this menuBar  
- Attach a QToolBar() to the QMainWindow() and addActions() to this Toolbar
- Launch the EventLoop for the QApplication()

## Detailed explanation    
Checkout the [Github Wiki](https://github.com/poivronjaune/PyQt6-MainWindow/wiki) for detailed explanations with step by step learning. We also discuss some basic object-oriented principles.  

We hope you enjoy our presentation!

## References  
[PyQt6 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)  
[The Qt  Open Collaboration Effort](https://contribute.qt-project.org/)  
[The PyQt6 Package from Pypi](https://pypi.org/project/PyQt6/)  
[Riverbank Computing - Creator of Qt Framework](https://www.riverbankcomputing.com/software/pyqt/)  
[Python Guis tutorials on PyQt6](https://www.pythonguis.com/pyqt6-tutorial/)  
[Pyhton Tutprial on PyQt6](https://www.pythontutorial.net/pyqt/)  
[Coder's Legacy PyQt6 Tutorial Series](https://coderslegacy.com/python/pyqt6-tutorial-series/)  
[2015 PDF PyQt5.5 and 4](https://www.tutorialspoint.com/pyqt/pyqt_tutorial.pdf)


