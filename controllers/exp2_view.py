from PyQt5.QtWidgets import QWidget, QLabel, QInputDialog, QMessageBox, QTextEdit, QDialog

from ui_py.Exp2Window import Ui_Exp2Window

from service.exp2.array import *

global_arr = None
global_state = None


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
                output = '输入的数组为：' + str(global_arr)
                print_by_dialog(output)
            except ValueError:
                QMessageBox.warning(self, '错误', '请输入有效的整数数组，例如：1, 2, 3（英文逗号）')
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
        global global_state
        global_state = order_or_not(global_arr)
        # （输出0）、升序（输出1）、降序（输出2）、先升后降（输出3）、或先降后升（输出4）状态
        string = f"提示: （输出0）、升序（输出1）、降序（输出2）、先升后降（输出3）、或先降后升（输出4）状态.\n\n你的数组为{global_arr}\n\n该数组状态为: {global_state}"
        print_by_dialog(string)

    def q3(self):
        if global_arr is None:
            QMessageBox.warning(self, '提示', '请先完成问题1_生成数组！')
            return None

        n, ok = QInputDialog.getInt(self, '输入框', '请输入要查找的目标值：')
        if ok:

            element, closest_index, se_index, se_comparisons = sequential_search(global_arr, n)
            bi_index, bi_comparisons = binary_search(global_arr, n)
            te_index, te_comparisons = ternary_search(global_arr, n)
            in_index, in_comparisons = interpolation_search(global_arr, n)

            if global_state == 1:
                statement = "升序"
            elif global_state == 2:
                statement = "降序"
            else:
                statement = None

            # 结果汇总
            if element is None:
                string = f"你的元素{n}出现在{statement}的数组中。\n\n"
                string += f"数组是{global_arr}\n\n"
                string += f"你要查找的值{n}所在数组的索引为{se_index}。\n\n"
                string += f"顺序查找，关键词比较次数是{se_comparisons}\n"
                string += f"二分查找，关键词比较次数是{bi_comparisons}\n"
                string += f"三分查找，关键词比较次数是{te_comparisons}\n"
                string += f"插值查找，关键词比较次数是{in_comparisons}\n"
            else:
                string = f"你的元素{n}没有出现在{statement}的数组中。\n\n"
                string += f"数组是{global_arr}\n\n"
                string += f"最接近的值为{element}，索引为{closest_index}。\n\n"
                string += f"顺序查找，关键词比较次数是{se_comparisons}\n"
                string += f"二分查找，关键词比较次数是{bi_comparisons}\n"
                string += f"三分查找，关键词比较次数是{te_comparisons}\n"
                string += f"插值查找，关键词比较次数是{in_comparisons}\n"

            # 特殊情况，数组既不是升序也不是降序
            if statement is None:
                string = f"你的数组既不是升序也不是降序，不符合对比要求。\n"

            print_by_dialog(string)
        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容!')

    def q4(self):
        if global_arr is None:
            QMessageBox.warning(self, '提示', '请先完成问题1_生成数组！')
            return None

        n, ok = QInputDialog.getInt(self, '输入框', '请输入要查找的目标值：')

        if ok:
            element, closest_index, se_index, se_comparisons = sequential_search(global_arr, n)
            if element is None:
                string = f"你的元素{n}出现在数组中。\n\n"
                string += f"数组是{global_arr}\n\n"
                string += f"你要查找的值{n}所在数组的索引为{se_index}。\n\n"
                string += f"关键词比较次数是{se_comparisons}\n"
            else:
                string = f"你的元素{n}没有出现在数组中。\n\n"
                string += f"数组是{global_arr}\n\n"
                string += f"最接近的值为{element}，索引为{closest_index}。\n\n"
                string += f"关键词比较次数是{se_comparisons}\n"

            print_by_dialog(string)
        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容!')

    def q5(self):
        if global_arr is None:
            QMessageBox.warning(self, '提示', '请先完成问题1_生成数组！')
            return None
        if global_state == 3:
            statement = "max"
        elif global_state == 4:
            statement = "min"
        elif global_state is None:
            QMessageBox.warning(self, '提示', '请先完成问题2,获得数组状态！')
            return None
        else:
            statement = None

        if statement is None:
            QMessageBox.warning(self, '提示', '你的数组不是先升后降或者先降后升的数组！请重新生成数组！')
            return None
        else:
            # 求最大值——二分法，三分法
            if statement == "max":
                value, index, bi_comparisons = binary_search_peak(global_arr)
                _, _, te_comparisons = ternary_search_peak(global_arr)
                string = f"你的数组是先升后降的数组。\n\n"
                string += f"数组是{global_arr}\n\n"
                string += f"最大值为{value}，索引为{index} \n\n"
                string += f"二分查找，关键词比较次数是{bi_comparisons}\n"
                string += f"三分查找，关键词比较次数是{te_comparisons}\n"
            # 求最小值——二分法，三分法
            elif statement == "min":
                value, index, bi_comparisons = binary_search_valley(global_arr)
                _, _, te_comparisons = ternary_search_valley(global_arr)
                string = f"你的数组是先降后升的数组。\n\n"
                string += f"数组是{global_arr}\n\n"
                string += f"最小值为{value}，索引为{index} \n\n"
                string += f"二分查找，关键词比较次数是{bi_comparisons}\n"
                string += f"三分查找，关键词比较次数是{te_comparisons}\n"
            # 将结果显示在对话框中
            print_by_dialog(string)

    def q6(self):
        if global_arr is None:
            QMessageBox.warning(self, '提示', '请先完成问题1_生成数组！')
            return None
        elif global_state is None:
            QMessageBox.warning(self, '提示', '请先完成问题2,获得数组状态！')
            return None
        elif global_state != 0:
            QMessageBox.warning(self, '提示', '需要无序数组，重新输入！')
            return None

        n, ok = QInputDialog.getInt(self, '输入框', '输入你要获取的第k个最小元素的k值：')
        if ok:
            value, br_comparisons = brute_force_kth_smallest(global_arr, n)
            _, so_comparisons = sorted_kth_smallest(global_arr, n)
            _, qu_comparisons = quickselect_kth_smallest(global_arr, n)
            string = f"你的数组是无序的数组。\n\n"
            string += f"数组是{global_arr}\n\n"
            string += f"第{n}小的元素为{value} \n\n"
            string += f"暴力查找，关键词比较次数是{br_comparisons}\n"
            string += f"排序查找，关键词比较次数是{so_comparisons}\n"
            string += f"快速选择查找，关键词比较次数是{qu_comparisons}\n"
            print_by_dialog(string)
        else:
            QMessageBox.warning(self, '提示', '没有输入任何内容!')
