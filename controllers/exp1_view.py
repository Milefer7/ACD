from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox, QTextEdit, QDialog
from PyQt5.QtGui import QPixmap
from ui_py.Exp1Window import Ui_Exp1Window
from ui_py.Exp1_q1 import Ui_Dialog
from service.exp1 import fibonacci
from service.exp1.fibonacci import *


def print_by_dialog(output):
    # 创建一个新的对话框
    dialog = Exp1Dialog()
    dialog.setText(output)
    dialog.exec_()


class Exp1Window(QWidget, Ui_Exp1Window):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # 保存主窗口的引用
        self.setupUi(self)

        # 点击 pushButton_1_out 跳转回主窗口
        self.pushButton_exp1_out.clicked.connect(self.go_back_to_main)

        # q1 点击进入按钮 弹出输入框
        self.pushButton_q1.clicked.connect(self.q1)

        # q2 点击进入按钮 开始运行
        self.pushButton_q2.clicked.connect(self.q2)

        # q3 点击进入按钮 开始运行
        self.pushButton_q3.clicked.connect(self.q3)

        # q4 点击进入按钮 弹出输入框
        self.pushButton_q4.clicked.connect(self.q4)

        # q5 递归
        self.pushButton_q5_recur.clicked.connect(self.q5_recursive)
        # q5 迭代
        self.pushButton_q5_inter.clicked.connect(self.q5_interation)

    # 显示主窗口并隐藏当前的 exp1 窗口
    def go_back_to_main(self):
        self.main_window.show_main_window()  # 调用主窗口中的方法显示主窗口
        self.hide()  # 隐藏 exp1 窗口

    def q1(self):
        # 用户点击了 OK，接下来获取斐波那契数的输入
        num, ok = QInputDialog.getInt(self, '输入框', '请输入要计算的第n个斐波那契数：')

        if ok:
            output = question1_output_qt(num)
            print_by_dialog(output)

        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容!')

    def q2(self):
        # QMessageBox.warning(self, '提示', '正在计算最大支持的斐波那契数，请稍等...计算完成后会弹出对话框！')
        max_num, time_consuming = question2_output_qt()
        output = f"不超过64位整数最大值的斐波那契数为第 {max_num} 个\n\n" \
                 f"执行时间: {time_consuming:.6f} 秒"
        print_by_dialog(output)

    def q3(self):
        QMessageBox.warning(self, '提示', '正在计算最大支持的斐波那契数(17分钟左右)，请稍等...计算完成后会弹出对话框！')
        max_num, time_consuming = question3_output_qt()
        output = f"不超过64位整数最大值的斐波那契数为第 {max_num} 个\n\n" \
                 f"执行时间: {time_consuming:.6f} 秒"
        print_by_dialog(output)

    def q4(self):
        QMessageBox.warning(self, '提示', '正在计算最大支持的 92号 斐波那契数，请稍等...计算完成后会弹出对话框！')
        count, max_num, time_consuming = question4_output_qt()
        output = f"不超过64位整数最大值的第 {count} 个斐波那契数为 {max_num}\n\n" \
                 f"执行时间: {time_consuming:.6f} 秒"
        print_by_dialog(output)

    def q5_recursive(self):
        QMessageBox.warning(self, '提示', '需要30s时间请稍等...计算完成后会弹出对话框！')
        count, time_consuming, detail = question5_recursive_output_qt()
        output = f"递归算法，30s内最大支持的斐波那契数是第 {count} 个\n\n" \
                 f"计算下一个斐波那契数耗时 {time_consuming:.6f} 秒"
        detail = detail + '\n\n' + output
        print_by_dialog(detail)

    def q5_interation(self):
        count, max_num, time_consuming = question5_recursive_output_qt()
        QMessageBox.warning(self, '提示', '需要30s时间请稍等...计算完成后会弹出对话框！')
        output = f"迭代算法，30s内最大支持的斐波那契数是第 {count} 个\n\n" \
                 f"计算下一个斐波那契数耗时 {time_consuming:.6f} 秒"
        print_by_dialog(output)


class Exp1Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setText(self, text):
        self.textEdit.setText(text)
