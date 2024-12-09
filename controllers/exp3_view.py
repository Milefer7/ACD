from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox, QTextEdit, QDialog
from PyQt5 import QtWidgets, QtCore
from ui_py.Exp3Window import Ui_Exp3Window
from ui_py.Exp3_q1_dialog import Ui_Dialog_exp3_q1
from service.exp3.bag import *


class Exp3Window(QWidget, Ui_Exp3Window):
    def __init__(self, main_window):
        super().__init__()

        # eg：
        # 物品的数量是： 3
        # 物品的价值和重量是： [(1, 1), (2, 2), (3, 3)]
        self.capacity = None
        self.item_num = None
        self.items = []

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
        self.item_num, ok = QInputDialog.getInt(self, '输入框', '请输入物品个数：')
        # print("item_num的类型是：", type(self.item_num))
        if ok:
            try:
                if self.item_num <= 0:
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
            ui.tableWidget.setRowCount(self.item_num)
            # 填充物品编号
            for i in range(self.item_num):
                item = QtWidgets.QTableWidgetItem(str(i + 1))  # 创建一个item, QTableWidgetItem表示一个表格单元， str(i + 1)表示单元格内容
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # 居中
                ui.tableWidget.setItem(i, 0, item)  # 设置单元格内容, 传入行数，列数，item

            ui.pushButton_submit_data.clicked.connect(lambda: self.submit_data(ui, self.item_num))
            # 缩小窗口
            # dialog.resize(422, 290)
            dialog.show()

        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容！')
            return

    def q2(self):
        capacity, ok = QInputDialog.getInt(self, '输入框', '请输入背包最大容量：')
        self.capacity = capacity
        print("背包的容量是：", self.capacity)
        if ok:
            try:
                if capacity <= 0:
                    QMessageBox.warning(self, '错误', '请输入一个正整数！')
                    return
            except ValueError:
                QMessageBox.warning(self, '错误', '请输入一个有效的整数！')
                return
            max_value, max_weight = greedy_fractional(capacity, self.items)
            print(f'q2结果：最大价值为：{max_value}，最终背包重量为：{max_weight}，时间复杂度为 O(nlogn)。')
            QMessageBox.information(self, 'q2结果',
                                    f'最大价值为：{max_value}，最终背包重量为：{max_weight}，时间复杂度为 O(nlogn)。')

        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容！')
            return

    def q3(self):
        if self.capacity is None:
            QMessageBox.warning(self, '错误', '请先完成q2，输入背包的容量！')
            return
        max_value, max_weight = greedy_01(self.capacity, self.items)
        print(f'q3结果：实例的近似解：最大价值为：{max_value}，最终背包重量为：{max_weight}。')
        QMessageBox.information(self, '结果', f'实例的近似解：最大价值为：{max_value}，最终背包重量为：{max_weight}。')

    def q4(self):
        if self.capacity is None:
            QMessageBox.warning(self, '错误', '请先完成q2，输入背包的容量！')
            return
        max_value, max_weight = brute_01(self.capacity, self.items)
        print(f'q4结果：实例的最优解：最大价值为：{max_value}，最终背包重量为：{max_weight}， 时间复杂度为 O(2^n)。')
        QMessageBox.information(self, '结果', f'实例的最优解：最大价值为：{max_value}，最终背包重量为：{max_weight}， 时间复杂度为 O(2^n)。')

    def q5(self):
        if self.capacity is None:
            QMessageBox.warning(self, '错误', '请先完成q2，输入背包的容量！')
            return
        max_value, max_weight = dynamic_01(self.capacity, self.items)
        print(f'q5结果：实例的最优解：最大价值为：{max_value}，最终背包重量为：{max_weight}， 时间复杂度为 O(nW)。')
        QMessageBox.information(self, '结果', f'实例的最优解：最大价值为：{max_value}，最终背包重量为：{max_weight}， 时间复杂度为 O(nW)。')

    def q6(self):
        if self.capacity is None:
            QMessageBox.warning(self, '错误', '请先完成q2，输入背包的容量！')
            return
        max_value, max_weight = dynamic_memory_01(self.capacity, self.items)
        print(f'q6结果：实例的最优解：最大价值为：{max_value}，最终背包重量为：{max_weight}， 时间复杂度为 O(nW)。')
        QMessageBox.information(self, '结果', f'实例的最优解：最大价值为：{max_value}，最终背包重量为：{max_weight}， 时间复杂度为 O(nW)。')

    def submit_data(self, ui, n):
        for i in range(n):
            try:
                value_item = ui.tableWidget.item(i, 1)
                weight_item = ui.tableWidget.item(i, 2)
                # print("调试1")
                if value_item is None or weight_item is None or not value_item.text() or not weight_item.text():
                    QMessageBox.warning(self, '错误', '有未填写的空，请重新输入！')
                    return

                value = int(value_item.text())
                weight = int(weight_item.text())
                # print("调试2")
                self.items.append((value, weight))
                # print("调试3")
            except ValueError:
                QMessageBox.warning(self, '错误', '请输入有效的整数，请重新输入！')
                return

        print("实验3 调试信息：")
        print("物品的数量是：", self.item_num)
        print("物品的价值和重量是：", self.items)

        QMessageBox.information(self, '提示', '数据提交成功！')
        # ui.close()
