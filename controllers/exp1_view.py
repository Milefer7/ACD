from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox, QTextEdit
from PyQt5.QtGui import QPixmap
from ui_py.Exp1Window import Ui_Exp1Window
from service.exp1 import fibonacci
from service.exp1.fibonacci import question1_output_qt


class Exp1Window(QWidget, Ui_Exp1Window):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # 保存主窗口的引用
        self.setupUi(self)

        # 点击 pushButton_1_out 跳转回主窗口
        self.pushButton_exp1_out.clicked.connect(self.go_back_to_main)

        # 点击点击进入按钮 弹出输入框
        self.pushButton_q1.clicked.connect(self.q1_user_input)

    # 显示主窗口并隐藏当前的 exp1 窗口
    def go_back_to_main(self):
        self.main_window.show_main_window()  # 调用主窗口中的方法显示主窗口
        self.hide()  # 隐藏 exp1 窗口

    def q1_user_input(self):
        num, ok = QInputDialog.getInt(self, '输入框', '请输入要计算的第n个斐波那契数：')

        if ok and num:
            self.show_calculate_fibonacci(num)
        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容!')

        # 计算并显示斐波那契数的输出
    def show_calculate_fibonacci(self, n):
        # 调用计算函数并获取输出字符串
        output = question1_output_qt(n)
        print(output)

        # 在 QTextEdit 中显示输出
        self.text_edit.setPlainText(output)
