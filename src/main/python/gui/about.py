# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui\about.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName("about")
        about.resize(250, 110)
        self.label = QtWidgets.QLabel(about)
        self.label.setGeometry(QtCore.QRect(125, 10, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(about)
        self.label_2.setGeometry(QtCore.QRect(125, 45, 110, 45))
        self.label_2.setObjectName("label_2")
        self.imageLabel = QtWidgets.QLabel(about)
        self.imageLabel.setGeometry(QtCore.QRect(15, 15, 90, 82))
        self.imageLabel.setObjectName("imageLabel")

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        _translate = QtCore.QCoreApplication.translate
        about.setWindowTitle(_translate("about", "About"))
        self.label.setText(_translate("about", "dsgui"))
        self.label_2.setText(_translate("about", "Copyright (c) 2021\n"
"Daren Liang\n"
"daren@darenliang.com"))
