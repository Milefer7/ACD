from PyQt5.QtWidgets import QWidget

from view.qt_designer.Exp1Window import Ui_Exp1Window


class Exp1Window(QWidget, Ui_Exp1Window):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # 保存主窗口的引用
        self.setupUi(self)

        # 点击 pushButton_1_out 跳转回主窗口
        self.pushButton_exp1_out.clicked.connect(self.go_back_to_main)

    # 显示主窗口并隐藏当前的 exp1 窗口
    def go_back_to_main(self):
        self.main_window.show_main_window()  # 调用主窗口中的方法显示主窗口
        self.hide()  # 隐藏 exp1 窗口
