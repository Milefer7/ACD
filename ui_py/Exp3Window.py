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
        Exp3Window.resize(828, 829)
        self.pushButton_exp3_out = QtWidgets.QPushButton(Exp3Window)
        self.pushButton_exp3_out.setGeometry(QtCore.QRect(680, 770, 111, 31))
        self.pushButton_exp3_out.setObjectName("pushButton_exp3_out")
        self.label = QtWidgets.QLabel(Exp3Window)
        self.label.setGeometry(QtCore.QRect(30, 10, 1021, 811))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imgs/实验3.png"))
        self.label.setObjectName("label")
        self.pushButton_q1 = QtWidgets.QPushButton(Exp3Window)
        self.pushButton_q1.setGeometry(QtCore.QRect(120, 140, 91, 41))
        self.pushButton_q1.setObjectName("pushButton_q1")
        self.pushButton_q2 = QtWidgets.QPushButton(Exp3Window)
        self.pushButton_q2.setGeometry(QtCore.QRect(120, 250, 91, 41))
        self.pushButton_q2.setObjectName("pushButton_q2")
        self.pushButton_q3 = QtWidgets.QPushButton(Exp3Window)
        self.pushButton_q3.setGeometry(QtCore.QRect(120, 390, 91, 41))
        self.pushButton_q3.setObjectName("pushButton_q3")
        self.pushButton_q4 = QtWidgets.QPushButton(Exp3Window)
        self.pushButton_q4.setGeometry(QtCore.QRect(120, 510, 91, 41))
        self.pushButton_q4.setObjectName("pushButton_q4")
        self.pushButton_q5 = QtWidgets.QPushButton(Exp3Window)
        self.pushButton_q5.setGeometry(QtCore.QRect(120, 630, 91, 41))
        self.pushButton_q5.setObjectName("pushButton_q5")
        self.pushButton_q6 = QtWidgets.QPushButton(Exp3Window)
        self.pushButton_q6.setGeometry(QtCore.QRect(120, 740, 91, 41))
        self.pushButton_q6.setObjectName("pushButton_q6")
        self.label.raise_()
        self.pushButton_exp3_out.raise_()
        self.pushButton_q1.raise_()
        self.pushButton_q2.raise_()
        self.pushButton_q3.raise_()
        self.pushButton_q4.raise_()
        self.pushButton_q5.raise_()
        self.pushButton_q6.raise_()

        self.retranslateUi(Exp3Window)
        QtCore.QMetaObject.connectSlotsByName(Exp3Window)

    def retranslateUi(self, Exp3Window):
        _translate = QtCore.QCoreApplication.translate
        Exp3Window.setWindowTitle(_translate("Exp3Window", "实验3"))
        self.pushButton_exp3_out.setText(_translate("Exp3Window", "返回主窗口"))
        self.pushButton_q1.setText(_translate("Exp3Window", "点击输入"))
        self.pushButton_q2.setText(_translate("Exp3Window", "点击输入"))
        self.pushButton_q3.setText(_translate("Exp3Window", "点击跳转"))
        self.pushButton_q4.setText(_translate("Exp3Window", "点击跳转"))
        self.pushButton_q5.setText(_translate("Exp3Window", "点击跳转"))
        self.pushButton_q6.setText(_translate("Exp3Window", "点击跳转"))
import res_rc
