# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Exp3_q1_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_exp3_q1(object):
    def setupUi(self, Dialog_exp3_q1):
        Dialog_exp3_q1.setObjectName("Dialog_exp3_q1")
        Dialog_exp3_q1.resize(422, 290)
        self.pushButton_submit_data = QtWidgets.QPushButton(Dialog_exp3_q1)
        self.pushButton_submit_data.setGeometry(QtCore.QRect(280, 250, 98, 26))
        self.pushButton_submit_data.setObjectName("pushButton_submit_data")
        self.tableWidget = QtWidgets.QTableWidget(Dialog_exp3_q1)
        self.tableWidget.setGeometry(QtCore.QRect(50, 40, 331, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(Dialog_exp3_q1)
        QtCore.QMetaObject.connectSlotsByName(Dialog_exp3_q1)

    def retranslateUi(self, Dialog_exp3_q1):
        _translate = QtCore.QCoreApplication.translate
        Dialog_exp3_q1.setWindowTitle(_translate("Dialog_exp3_q1", "Dialog"))
        self.pushButton_submit_data.setText(_translate("Dialog_exp3_q1", "提交数据"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_exp3_q1", "物品编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_exp3_q1", "物品价值"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_exp3_q1", "物品重量"))