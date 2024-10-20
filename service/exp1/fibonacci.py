# 五种方法：1.迭代、2.迭代改进、3.递归、4.显示公式、5.矩阵
# 1、1、2、3、5、8、13、21、34
import time
import math
import numpy as np


# Fibonacci 迭代，空间复杂度为线性
def fibo1_iteration(num):
    """
    计算第 num 个斐波那契数，使用迭代方法，空间复杂度为线性。

    :param num: 计算的斐波那契数的索引
    :return: 第 num 个斐波那契数、基本操作、基本操作次数、运行时间、空间效率
    """
    operations = 0  # 操作计数器
    start_time = time.perf_counter()  # 开始计时

    if num < 2:
        execution_time = f"{time.perf_counter() - start_time:.6f}"
        return num, '加法', operations, execution_time, "线性"

    arr = [0] * (num + 1)  # 创建数组以存储中间结果
    arr[0], arr[1] = 0, 1  # 基线条件

    # 开始迭代
    for i in range(2, num + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
        operations += 1  # 计数加法操作

    execution_time = f"{time.perf_counter() - start_time:.6f}"  # 计算运行时间
    return arr[-1], '加法', operations, execution_time, "线性"


# Fibonacci 迭代，空间复杂度为常数
def fibo2_iteration(num):
    """
    计算第 num 个斐波那契数，使用迭代方法，空间复杂度为常数。

    :param num: 计算的斐波那契数的索引
    :return: 第 num 个斐波那契数、基本操作、基本操作次数、运行时间、空间效率
    """
    operations = 0  # 操作计数器
    start_time = time.perf_counter()  # 开始计时

    if num < 2:
        execution_time = f"{time.perf_counter() - start_time:.6f}"
        return num, '加法', operations, execution_time, "常数"

    one_before, two_before = 1, 0  # 前两个斐波那契数

    # 开始迭代
    for _ in range(2, num + 1):
        one_before, two_before = one_before + two_before, one_before
        operations += 1  # 计数加法操作

    execution_time = f"{time.perf_counter() - start_time:.6f}"  # 计算运行时间
    return one_before, '加法', operations, execution_time, "常数"


# Fibonacci 递归
def fibo3_recursion(num):
    """
    计算第 num 个斐波那契数，使用递归方法。

    :param num: 计算的斐波那契数的索引
    :return: 第 num 个斐波那契数、基本操作、基本操作次数、运行时间、空间效率
    """
    operations = 0  # 操作计数器
    start_time = time.perf_counter()  # 开始计时

    def recursive_fib(n):
        nonlocal operations
        if n < 2:
            return n
        else:
            operations += 1  # 计数加法操作
            return recursive_fib(n - 1) + recursive_fib(n - 2)

    result = recursive_fib(num)
    execution_time = f"{time.perf_counter() - start_time:.6f}"  # 计算运行时间
    return result, '加法', operations, execution_time, "常数"


# Fibonacci 公式
def fibo4_formula(num):
    """
    计算第 num 个斐波那契数，使用公式方法。

    :param num: 计算的斐波那契数的索引
    :return: 第 num 个斐波那契数、基本操作、基本操作次数、运行时间、空间效率
    """
    start_time = time.perf_counter()  # 开始计时
    operation = 2 * num + 6
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2  # 黄金分割比
    psi = (1 - sqrt_5) / 2  # 另一个根

    result = int((phi ** num - psi ** num) / sqrt_5)
    execution_time = f"{time.perf_counter() - start_time:.6f}"  # 计算运行时间
    return result, '乘法', operation, execution_time, "常数"  # 公式计算不涉及操作次数


def fibo5_matrix(num):
    """
    计算第 num 个斐波那契数，使用矩阵方法。

    :param num: 计算的斐波那契数的索引
    :return: 第 num 个斐波那契数、基本操作、基本操作次数、运行时间、空间效率
    """
    start_time = time.perf_counter()  # 开始计时
    operations = int(8 * (math.log2(num) + 1))
    if num < 2:
        execution_time = f"{time.perf_counter() - start_time:.6f}"
        return num, '乘法', 0, execution_time, "常数"

    # 定义斐波那契数的转移矩阵
    F = np.array([[1, 1],
                  [1, 0]])

    # 矩阵快速幂
    def matrix_pow(matrix, n):
        result = np.identity(2)  # 单位矩阵

        while n:
            if n % 2:  # 如果 n 是奇数
                result = np.dot(result, matrix)  # 进行矩阵乘法
            matrix = np.dot(matrix, matrix)  # 平方矩阵
            n //= 2  # 除以 2

        return result

    # 计算 F^(n-1)
    result_matrix = matrix_pow(F, num - 1)

    # 第 num 个斐波那契数为矩阵的 [0][0] 元素
    result = result_matrix[0][0]
    execution_time = f"{time.perf_counter() - start_time:.6f}"  # 计算运行时间

    return int(result), '乘法', operations, execution_time, "常数"


def question1_output_cmd(n):
    print(f"计算第 {n} 个斐波那契数：")

    # 调用第一种方法：迭代（空间复杂度线性）
    result1 = fibo1_iteration(n)
    print(f"1. 迭代：结果={result1[0]}, 操作类型={result1[1]}, 操作次数={result1[2]}, "
          f"运行时间={result1[3]} 秒, 空间复杂度={result1[4]}")

    # 调用第二种方法：迭代（空间复杂度常数）
    result2 = fibo2_iteration(n)
    print(f"2. 迭代：结果={result2[0]}, 操作类型={result2[1]}, 操作次数={result2[2]}, "
          f"运行时间={result2[3]} 秒, 空间复杂度={result2[4]}")

    # 调用第三种方法：递归
    result3 = fibo3_recursion(n)
    print(f"3. 递归：结果={result3[0]}, 操作类型={result3[1]}, 操作次数={result3[2]}, "
          f"运行时间={result3[3]} 秒, 空间复杂度={result3[4]}")

    # 调用第四种方法：公式
    result4 = fibo4_formula(n)
    print(f"4. 公式：结果={result4[0]}, 操作类型={result4[1]}, 操作次数={result4[2]}, "
          f"运行时间={result4[3]} 秒, 空间复杂度={result4[4]}")

    # 调用第五种方法：矩阵
    result5 = fibo5_matrix(n)
    print(f"5. 矩阵：结果={result5[0]}, 操作类型={result5[1]}, 操作次数={result5[2]}, "
          f"运行时间={result5[3]} 秒, 空间复杂度={result5[4]}")


def question1_output_qt(n):
    output = f"计算第 {n} 个斐波那契数：\n"

    # 调用第一种方法：迭代（空间复杂度线性）
    result1 = fibo1_iteration(n)
    output += f"1. 迭代：结果={result1[0]}, 操作类型={result1[1]}, 操作次数={result1[2]}, " \
              f"运行时间={result1[3]} 秒, 空间复杂度={result1[4]}\n"

    # 调用第二种方法：迭代（空间复杂度常数）
    result2 = fibo2_iteration(n)
    output += f"2. 迭代：结果={result2[0]}, 操作类型={result2[1]}, 操作次数={result2[2]}, " \
              f"运行时间={result2[3]} 秒, 空间复杂度={result2[4]}\n"

    # 调用第三种方法：递归
    result3 = fibo3_recursion(n)
    output += f"3. 递归：结果={result3[0]}, 操作类型={result3[1]}, 操作次数={result3[2]}, " \
              f"运行时间={result3[3]} 秒, 空间复杂度={result3[4]}\n"

    # 调用第四种方法：公式
    result4 = fibo4_formula(n)
    output += f"4. 公式：结果={result4[0]}, 操作类型={result4[1]}, 操作次数={result4[2]}, " \
              f"运行时间={result4[3]} 秒, 空间复杂度={result4[4]}\n"

    # 调用第五种方法：矩阵
    result5 = fibo5_matrix(n)
    output += f"5. 矩阵：结果={result5[0]}, 操作类型={result5[1]}, 操作次数={result5[2]}, " \
              f"运行时间={result5[3]} 秒, 空间复杂度={result5[4]}\n"

    return output


if __name__ == "__main__":
    n_values = [1, 10, 20, 30]  # 测试的斐波那契数列位置

    for n in n_values:
        question1_output(n)
        print("-" * 50)  # 分割线
