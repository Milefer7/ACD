# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exp2Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exp2Window(object):
    def setupUi(self, Exp2Window):
        Exp2Window.setObjectName("Exp2Window")
        Exp2Window.resize(398, 299)
        self.pushButton_exp2_out = QtWidgets.QPushButton(Exp2Window)
        self.pushButton_exp2_out.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.pushButton_exp2_out.setObjectName("pushButton_exp2_out")

        self.retranslateUi(Exp2Window)
        QtCore.QMetaObject.connectSlotsByName(Exp2Window)

    def retranslateUi(self, Exp2Window):
        _translate = QtCore.QCoreApplication.translate
        Exp2Window.setWindowTitle(_translate("Exp2Window", "实验2"))
        self.pushButton_exp2_out.setText(_translate("Exp2Window", "返回主窗口"))
