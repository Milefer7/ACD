from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox, QTextEdit, QDialog
from PyQt5.QtGui import QPixmap
from ui_py.Exp1Window import Ui_Exp1Window
from ui_py.Exp1_q1 import Ui_Dialog
from service.exp1 import fibonacci
from service.exp1.fibonacci import question1_output_qt


class Exp1Window(QWidget, Ui_Exp1Window):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # 保存主窗口的引用
        self.setupUi(self)

        # 点击 pushButton_1_out 跳转回主窗口
        self.pushButton_exp1_out.clicked.connect(self.go_back_to_main)

        # q1 点击点击进入按钮 弹出输入框
        self.pushButton_q1.clicked.connect(self.q1_user_input)

        # 点击 pu

    # 显示主窗口并隐藏当前的 exp1 窗口
    def go_back_to_main(self):
        self.main_window.show_main_window()  # 调用主窗口中的方法显示主窗口
        self.hide()  # 隐藏 exp1 窗口

    def q1_user_input(self):
        # 用户点击了 OK，接下来获取斐波那契数的输入
        num, ok = QInputDialog.getInt(self, '输入框', '请输入要计算的第n个斐波那契数：')

        if ok:
            self.show_calculate_fibonacci(num)
        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容!')

    def show_calculate_fibonacci(self, n):
        # 调用计算函数并获取输出字符串
        output = question1_output_qt(n)

        # 创建一个新的对话框
        dialog = Exp1Dialog()
        dialog.setText(output)
        dialog.exec_()


class Exp1Dialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setText(self, text):
        self.textEdit.setText(text)


