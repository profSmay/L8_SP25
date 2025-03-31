#region imports
import numpy as np
import matplotlib.pyplot as plt

import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc

from Aero_Demo_ui import Ui_Dialog
from Wing_Class import Wing
#endregion

#region class definitions
class main_window(qtw.QDialog, Ui_Dialog):
    def __init__(self):
        '''
        Constructor for main_window.  This is a little different than inheriting from
        QWidgit, though QDialog inherits from QWidgit.
        '''
        super(main_window,self).__init__()
        self.setupUi(self)  # This function is created in pyuic5 translation of ui file to py file.
        #signals and slots are assigned in this function
        self.assign_widgets()
        self.wing=None  # the primary data element for this program
        self.show()
    def assign_widgets(self):
        '''
        connect signals and slots
        :return:
        '''
        self.pushButton_Exit.clicked.connect(self.ExitApp)
        self.pushButton_GetWing.clicked.connect(self.GetWing)
        self.comboBox.currentTextChanged.connect(self.combobox_changed)
        #add some choices to the comboBox
        self.comboBox.addItem("Birch")
        self.comboBox.addItem("Oak")
        self.comboBox.addItem("Sycamore")
    def combobox_changed(self):
        '''
        Slot for comboBox currentTextChanged
        :return:
        '''
        text = self.comboBox.currentText()
        self.lineEdit_fromCombo.setText(text)
        pass
    def GetWing(self):
        # get the filename using the OPEN dialog
        filename=qtw.QFileDialog.getOpenFileName()[0]
        if len(filename)==0: 
            self.no_file()
            return
        self.textEdit_filename.setText(filename)
        #we do this in case it takes a long time to read the file
        qtw.QApplication.setOverrideCursor(qtc.Qt.WaitCursor)

        # Read the file
        f1 = open(filename, 'r')  # open the file for reading
        data = f1.readlines()  # read the entire file as a list of strings
        f1.close()  # close the file  ... very important

        self.wing=Wing()  # create a wing instance (object)

        try:  #an example of handling an error
            self.wing.processWingData(data)
            self.lineEdit_Height.setText('{:.2f}'.format(self.wing.sparH))
            self.lineEdit_Width.setText('{:.2f}'.format(self.wing.sparW))
            report = self.wing.generate_report()
            self.plainTextEdit_Report.setPlainText(report)

            qtw.QApplication.restoreOverrideCursor()
        except:
            qtw.QApplication.restoreOverrideCursor()
            self.bad_file()
    def no_file(self):
        msg = qtw.QMessageBox()
        msg.setText('There was no file selected')
        msg.setWindowTitle("No File")
        retval = msg.exec_()
        return None
    def bad_file(self):
        msg = qtw.QMessageBox()
        msg.setText('Unable to process the selected file')
        msg.setWindowTitle("Bad File")
        retval = msg.exec_()
        return

    def PlotSomething(self):
        x=np.linspace(0,6*np.pi,300)
        y=np.zeros_like(x)
        for i in range(300):
            y[i]=np.exp(-x[i]/5)*np.sin(x[i])
        plt.plot(x,y)
        plt.show()
        return
    def ExitApp(self):
        app.exit()
#endregion

if __name__ == "__main__":
    app = qtw.QApplication.instance()
    if not app:
        app = qtw.QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())
    
 





