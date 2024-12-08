from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox, QTextEdit, QDialog
from PyQt5 import QtWidgets, QtCore
from ui_py.Exp3Window import Ui_Exp3Window
from ui_py.Exp3_q1_dialog import Ui_Dialog_exp3_q1


class Exp3Window(QWidget, Ui_Exp3Window):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # 保存主窗口的引用
        self.setupUi(self)

        # 点击 pushButton_1_out 跳转回主窗口
        self.pushButton_exp3_out.clicked.connect(self.go_back_to_main)

        # q1 点击进入按钮 开始运行
        self.pushButton_q1.clicked.connect(self.q1)
        # q2 点击进入按钮 开始运行
        self.pushButton_q2.clicked.connect(self.q2)
        # q3 点击进入按钮 开始运行
        self.pushButton_q3.clicked.connect(self.q3)
        # q4 点击进入按钮 开始运行
        self.pushButton_q4.clicked.connect(self.q4)
        # q5 点击进入按钮 开始运行
        self.pushButton_q5.clicked.connect(self.q5)
        # q6 点击进入按钮 开始运行
        self.pushButton_q6.clicked.connect(self.q6)

    # 显示主窗口并隐藏当前的 exp1 窗口
    def go_back_to_main(self):
        self.main_window.show_main_window()  # 调用主窗口中的方法显示主窗口
        self.hide()  # 隐藏 exp1 窗口

    def q1(self):
        item_num, ok = QInputDialog.getText(self, '输入框', '请输入物品个数：')
        if ok:
            try:
                n = int(item_num)
                if n <= 0:
                    QMessageBox.warning(self, '错误', '请输入一个正整数！')
                    return
            except ValueError:
                QMessageBox.warning(self, '错误', '请输入一个有效的整数！')
                return

            # 弹出Exp3_q1_dialog
            dialog = QDialog(self)
            ui = Ui_Dialog_exp3_q1()
            ui.setupUi(dialog)

            # 设置行数
            ui.tableWidget.setRowCount(n)
            # 填充物品编号
            for i in range(n):
                item = QtWidgets.QTableWidgetItem(str(i + 1))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                ui.tableWidget.setItem(i, 0, item)

            dialog.exec_()


        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容！')
            return

    def q2(self):
        pass

    def q3(self):
        pass

    def q4(self):
        pass

    def q5(self):
        pass

    def q6(self):
        pass
