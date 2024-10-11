from PyQt5.QtWidgets import QWidget, QMainWindow
from view.qt_designer.MainWindow import Ui_MainWindow # 导入主窗口UI
from view.qt_designer.Exp1Window import Ui_Exp1Window # 导入exp1窗口UI


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 创建 exp1 窗口的实例
        self.exp1_window = Exp1Window(self)

        # 按钮点击时跳转到 exp1 窗口
        self.pushButton_exp1_in.clicked.connect(self.show_exp1_window)

    # 显示 exp1 窗口并隐藏主窗口
    def show_exp1_window(self):
        self.exp1_window.show()
        self.hide()

    # 显示主窗口并隐藏 exp1 窗口（从 exp1 回到主窗口时使用）
    def show_main_window(self):
        self.show()


class Exp1Window(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window  # 保存主窗口的引用
        self.setupUi(self)

        # 点击 pushButton_1_out 跳转回主窗口
        self.pushButton_1_out.clicked.connect(self.go_back_to_main)

    # 显示主窗口并隐藏当前的 exp1 窗口
    def go_back_to_main(self):
        self.main_window.show_main_window()  # 调用主窗口中的方法显示主窗口
        self.hide()  # 隐藏 exp1 窗口