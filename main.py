import sys

from PyQt5.QtWidgets import QApplication
from controllers.main_view import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建并显示主窗口
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
