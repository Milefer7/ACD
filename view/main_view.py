from PyQt5.QtWidgets import QWidget, QMainWindow

from view.exp1_view import Exp1Window
from view.exp2_view import Exp2Window
from view.exp3_view import Exp3Window
from view.qt_designer.MainWindow import Ui_MainWindow  # 导入主窗口UI
from view.qt_designer.Exp1Window import Ui_Exp1Window  # 导入生成的 UI 类


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 创建 exp1 窗口的实例
        self.exp1_window = Exp1Window(self)
        # 按钮点击时跳转到 exp1 窗口
        self.pushButton_exp1_in.clicked.connect(self.show_exp1_window)

        # 创建 exp2 窗口的实例
        self.exp2_window = Exp2Window(self)
        # 按钮点击时跳转到 exp2 窗口
        self.pushButton_exp2_in.clicked.connect(self.show_exp2_window)

        # 创建 exp3 窗口的实例
        self.exp3_window = Exp3Window(self)
        # 按钮点击时跳转到 exp3 窗口
        self.pushButton_exp3_in.clicked.connect(self.show_exp3_window)

    # 显示 exp1 窗口并隐藏主窗口
    def show_exp1_window(self):
        self.exp1_window.show()
        self.hide()

    def show_exp2_window(self):
        self.exp1_window.show()
        self.hide()

    def show_exp3_window(self):
        self.exp1_window.show()
        self.hide()

    # 显示主窗口并隐藏 exp1 窗口（从 exp1 回到主窗口时使用）
    def show_main_window(self):
        self.show()
