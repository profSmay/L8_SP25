# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Aero_Demo_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 844)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_GetWing = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_GetWing.setObjectName("pushButton_GetWing")
        self.verticalLayout_2.addWidget(self.pushButton_GetWing)
        self.textEdit_filename = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_filename.setReadOnly(True)
        self.textEdit_filename.setObjectName("textEdit_filename")
        self.verticalLayout_2.addWidget(self.textEdit_filename)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_Height = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_Height.setObjectName("lineEdit_Height")
        self.horizontalLayout.addWidget(self.lineEdit_Height)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_Width = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_Width.setText("")
        self.lineEdit_Width.setObjectName("lineEdit_Width")
        self.horizontalLayout.addWidget(self.lineEdit_Width)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.lineEdit_fromCombo = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_fromCombo.setText("")
        self.lineEdit_fromCombo.setObjectName("lineEdit_fromCombo")
        self.horizontalLayout_2.addWidget(self.lineEdit_fromCombo)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plainTextEdit_Report = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_Report.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit_Report.setObjectName("plainTextEdit_Report")
        self.verticalLayout_3.addWidget(self.plainTextEdit_Report)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.verticalLayout.addWidget(self.pushButton_Exit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wing Spar Structural Optimization"))
        self.groupBox.setTitle(_translate("Dialog", "Input"))
        self.pushButton_GetWing.setText(_translate("Dialog", "Open and Read a Wing File a - as a Demo"))
        self.groupBox_3.setTitle(_translate("Dialog", "Spar I-beam Shape"))
        self.label.setText(_translate("Dialog", "Height"))
        self.label_2.setText(_translate("Dialog", "Width"))
        self.label_3.setText(_translate("Dialog", "was selected"))
        self.groupBox_2.setTitle(_translate("Dialog", "GroupBox"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))

