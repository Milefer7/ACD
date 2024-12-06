from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox, QTextEdit, QDialog

from ui_py.Exp2Window import Ui_Exp2Window

from service.exp2.array import *

global_arr = None


class Exp2Window(QWidget, Ui_Exp2Window):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # 保存主窗口的引用
        self.setupUi(self)

        # 点击 pushButton_2_out 跳转回主窗口
        self.pushButton_exp2_out.clicked.connect(self.go_back_to_main)

        # q1 点击进入按钮 弹出输入框
        self.pushButton_q1_user.clicked.connect(self.q1_user)
        self.pushButton_q1_random.clicked.connect(self.q1_random)

        # q2 点击进入按钮 开始运行
        self.pushButton_q2.clicked.connect(self.q2)

        # q3 点击进入按钮 开始运行
        self.pushButton_q3.clicked.connect(self.q3)

        # q4 点击进入按钮 弹出输入框
        self.pushButton_q4.clicked.connect(self.q4)

        # q5 递归
        self.pushButton_q5.clicked.connect(self.q5)

        # q6
        self.pushButton_q6.clicked.connect(self.q6)

    # 显示主窗口并隐藏当前的 exp1 窗口
    def go_back_to_main(self):
        self.main_window.show_main_window()  # 调用主窗口中的方法显示主窗口
        self.hide()  # 隐藏 exp1 窗口

    def q1_user(self):
        # 用户输入一个以逗号分隔的数组
        text, ok = QInputDialog.getText(self, '输入框', '请输入一个不重复的数组（用逗号分隔）：')

        if ok:
            try:
                # 将输入字符串解析为数组
                user_array = [int(x.strip()) for x in text.split(',')]
                global global_arr
                global_arr = user_array
                # 显示输入的数组
                output = '输入的数组为：\n' + str(global_arr)
                print_by_dialog(output)
            except ValueError:
                QMessageBox.warning(self, '错误', '请输入有效的整数数组，例如：1, 2, 3')
        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容!')

    def q1_random(self):
        # 用户点击了 OK，接下来获取斐波那契数的输入
        n, ok = QInputDialog.getInt(self, '输入框', '请输入要计算数组长度n：')

        if ok:
            global global_arr
            global_arr = gen_arr(n)
            # 把数组转换为字符串
            output = '生成的数组为：\n' + str(global_arr)
            print_by_dialog(output)

        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容!')

    def q2(self):
        if global_arr is None:
            QMessageBox.warning(self, '提示', '请先完成问题1_生成数组！')
            return None
        n = order_or_not(global_arr)
        # （输出0）、升序（输出1）、降序（输出2）、先升后降（输出3）、或先降后升（输出4）状态
        string = f"提示: （输出0）、升序（输出1）、降序（输出2）、先升后降（输出3）、或先降后升（输出4）状态.\n\n你的数组为{global_arr}\n\n该数组状态为: {n}"
        print_by_dialog(string)

    def q3(self):
        pass

    def q4(self):
        pass

    def q5(self):
        pass

    def q6(self):
        pass
