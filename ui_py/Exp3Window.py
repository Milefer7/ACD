# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exp3Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exp3Window(object):
    def setupUi(self, Exp3Window):
        Exp3Window.setObjectName("Exp3Window")
        Exp3Window.resize(400, 300)
        self.pushButton_exp3_out = QtWidgets.QPushButton(Exp3Window)
        self.pushButton_exp3_out.setGeometry(QtCore.QRect(290, 240, 75, 23))
        self.pushButton_exp3_out.setObjectName("pushButton_exp3_out")

        self.retranslateUi(Exp3Window)
        QtCore.QMetaObject.connectSlotsByName(Exp3Window)

    def retranslateUi(self, Exp3Window):
        _translate = QtCore.QCoreApplication.translate
        Exp3Window.setWindowTitle(_translate("Exp3Window", "实验3"))
        self.pushButton_exp3_out.setText(_translate("Exp3Window", "返回主窗口"))