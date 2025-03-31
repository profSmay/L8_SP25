#region imports
from MouseTracker import Ui_MouseTracker
from PyQt5 import uic
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
#endregion
#region class definitions
class MainWindow(qtw.QWidget, Ui_MouseTracker):
    def __init__(self):
        '''
        Main window constructor.
        1. This program demonstrates use of the PyQt EventFilter to capture and process window events
        2. A windows event is 'caught' by a particular widget based on 'focus'
        Step 1:  installEventFilter on PyQty objects (target) you want to handle events.
                 Note that GUI widgets are often stacked on top of eachother, so the closest to
                 the user catches the events first.
        Step 2:  when and event happens, handle it and pass it along to underlying widgets or stop the processing of the event
        '''
        super().__init__()
        self.setupUi(self)
        # Main UI code goes here
        #I'm installing an event filter because there is no signal for keypress
        self.spin_MouseTracker.installEventFilter(self)
        self.spin_MouseTracker.setMouseTracking(True)
        self.spin_MouseTracker.lineEdit().installEventFilter(self)
        self.spin_MouseTracker.lineEdit().setMouseTracking(True)
        self.pushButton.pressed.connect(self.colorButton)
        self.pushButton.installEventFilter(self)
        self.pushButton_2.installEventFilter(self)
        self.pushButton.setMouseTracking(True)
        self.pushButton_2.setMouseTracking(True)
        # end Main UI code
        self.show()  #show the main widget

    #since my main window is a widget, I can customize its events by overriding the default event
    def mouseMoveEvent(self, event):
        self.setWindowTitle('x:{}, y:{}'.format(event.x(), event.y()))

    def colorButton(self):
        self.pushButton.setAutoFillBackground(False)

    #the event filter allows me to respond to specific events for a specific object
    def eventFilter(self, source, event):
        if event.type()==qtc.QEvent.KeyPress:
            et=event.type()
            if event.key()==qtc.Qt.Key_Up:
                self.setWindowTitle('up pushed')
            if event.key() == qtc.Qt.Key_Down:
                self.setWindowTitle('down pushed')
            if event.key() == qtc.Qt.Key_O:
                self.setWindowTitle('Go Pokes!!')
            pass
        if event.type() == event.Enter:
            if source == self.pushButton:
                self.pushButton.setText("Over me")
            if source == self.pushButton_2:
                self.pushButton_2.setText("Over me")
        if event.type() == event.Leave:
            if source == self.pushButton:
                self.pushButton.setText("pushButton")
            if source == self.pushButton_2:
                self.pushButton_2.setText("pushButton2")
        # Handle MouseMove for spin_MouseTracker specifically because spinBox widget swallows MouseMove events
        if event.type() == qtc.QEvent.MouseMove and source in (self.spin_MouseTracker, self.spin_MouseTracker.lineEdit()):
            global_pos = source.mapToGlobal(event.pos())
            window_pos = self.mapFromGlobal(global_pos)
            self.setWindowTitle(f'x:{window_pos.x()}, y:{window_pos.y()}')

        return super(MainWindow, self).eventFilter(source, event)
#endregion

if __name__== '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.setWindowTitle('Mouse Tracker')
    sys.exit(app.exec())