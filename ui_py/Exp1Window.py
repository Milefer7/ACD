# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exp1Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exp1Window(object):
    def setupUi(self, Exp1Window):
        Exp1Window.setObjectName("Exp1Window")
        Exp1Window.resize(1052, 883)
        Exp1Window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Exp1Window.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_exp1_out = QtWidgets.QPushButton(Exp1Window)
        self.pushButton_exp1_out.setGeometry(QtCore.QRect(880, 820, 141, 51))
        self.pushButton_exp1_out.setCheckable(False)
        self.pushButton_exp1_out.setObjectName("pushButton_exp1_out")
        self.pushButton_q2 = QtWidgets.QPushButton(Exp1Window)
        self.pushButton_q2.setGeometry(QtCore.QRect(820, 120, 151, 71))
        self.pushButton_q2.setObjectName("pushButton_q2")
        self.label = QtWidgets.QLabel(Exp1Window)
        self.label.setGeometry(QtCore.QRect(10, 0, 1041, 881))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imgs/实验1.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton_q2.raise_()
        self.pushButton_exp1_out.raise_()

        self.retranslateUi(Exp1Window)
        QtCore.QMetaObject.connectSlotsByName(Exp1Window)

    def retranslateUi(self, Exp1Window):
        _translate = QtCore.QCoreApplication.translate
        Exp1Window.setWindowTitle(_translate("Exp1Window", "实验1"))
        self.pushButton_exp1_out.setText(_translate("Exp1Window", "返回主窗口"))
        self.pushButton_q2.setText(_translate("Exp1Window", "Q2:五种方法"))
import res_rc