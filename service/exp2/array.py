import random
from controllers.exp1_view import print_by_dialog


# 问题1
def gen_arr(n):
    # 要求：生成长度为 n 的数组，且元素不重复
    max_num = n * 10
    return random.sample(range(1, max_num), n)


# 问题2
def order_or_not(arr):
    # 要求：设计一个算法判断要求1中产生的整数数组是否为或未排序（输出0）、升序（输出1）、降序（输出2）、先升后降（输出3）、或先降后升（输出4）状态
    if arr == sorted(arr):
        return 1
    elif arr == sorted(arr, reverse=True):
        return 2

    # 检查是否先升后降
    if len(arr) != 2:
        peak = max(arr)
        peak_index = arr.index(peak)
        # print("peak_index: ", peak_index)
        if arr[:peak_index + 1] == sorted(arr[:peak_index + 1]) and arr[peak_index:] == sorted(arr[peak_index:],
                                                                                               reverse=True):
            return 3

    # 检查是否先降后升
    if len(arr) != 2:
        valley = min(arr)
        valley_index = arr.index(valley)
        if arr[:valley_index + 1] == sorted(arr[:valley_index + 1], reverse=True) and arr[valley_index:] == sorted(
                arr[valley_index:]):
            return 4

    return 0


# 问题3
# 顺序查找
def sequential_search(arr, target):
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == target:
            return None, None, i, comparisons  # 返回最近的元素，最近的位置，匹配到元素的位置，比较次数
    # 若没找到，返回最接近的元素和位置
    closest_index = min(range(len(arr)), key=lambda i: abs(arr[i] - target))
    return arr[closest_index], closest_index, None, comparisons


# 二分查找
def binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # closest_index = left if left < len(arr) else right
    return None, comparisons


# 三分查找
# 函数返回 元素索引, 比较次数
def ternary_search(arr, target):
    comparisons = 0

    def recursive_ternary_search(left, right):
        nonlocal comparisons
        # 如果搜索区间无效（左边界大于右边界）
        if left > right:
            # closest_index = left if left < len(arr) else right
            return None

        # 将搜索区间分成三个部分
        third = (right - left) // 3
        mid1, mid2 = left + third, right - third

        # 比较目标值与第一个三分点的值
        comparisons += 1
        if arr[mid1] == target:
            return mid1

        # 比较目标值与第二个三分点的值
        comparisons += 1
        if arr[mid2] == target:
            return mid2

        # 目标值在第一个三分点左侧
        if target < arr[mid1]:
            return recursive_ternary_search(left, mid1 - 1)

        # 目标值在两个三分点之间
        elif arr[mid1] < target < arr[mid2]:
            return recursive_ternary_search(mid1 + 1, mid2 - 1)

        # 目标值在第二个三分点右侧
        else:
            return recursive_ternary_search(mid2 + 1, right)

    # 启动递归查找，从整个数组范围开始
    return recursive_ternary_search(0, len(arr) - 1), comparisons


# 插值查找
def interpolation_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1

    # 当目标值在数组范围内时
    while left <= right and arr[left] <= target <= arr[right]:
        comparisons += 1

        # 处理特殊单元素情况
        if left == right:
            if arr[left] == target:
                return left, comparisons
            else:
                break

        # 计算插值位置，思想是根据目标值在整个数组范围内的相对位置，估算目标值在数组中的位置
        pos = left + ((target - arr[left]) * (right - left) // (arr[right] - arr[left]))

        comparisons += 1
        if arr[pos] == target:
            return pos, comparisons
        if arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    # closest_index = left if left < len(arr) else right
    return None, comparisons


# 问题4 直接复用问题三的顺序查找
# def linear_search(arr, target):
#     comparisons = 0
#     for i, value in enumerate(arr):
#         comparisons += 1
#         if value == target:
#             return i, comparisons
#     return -1, comparisons


# 问题5
# 【找最大值】二分查找
def binary_search_peak(arr):  # 返回值，索引，比较次数
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return arr[left], left, comparisons


# 【找最小值】二分查找
def binary_search_valley(arr):  # 返回值，索引，比较次数
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] < arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return arr[left], left, comparisons


# 【找最大值】三分查找
def ternary_search_peak(arr):  # 返回值，索引，比较次数
    comparisons = 0

    def recursive_search(left, right):
        nonlocal comparisons
        if left == right:
            return arr[left], left, comparisons

        third = (right - left) // 3
        mid1, mid2 = left + third, right - third

        comparisons += 1
        if arr[mid1] > arr[mid2]:
            return recursive_search(left, mid2 - 1)
        else:
            return recursive_search(mid1 + 1, right)

    return recursive_search(0, len(arr) - 1)


# 【找最小值】三分查找
def ternary_search_valley(arr):  # 返回值，索引，比较次数
    comparisons = 0

    def recursive_search(left, right):
        nonlocal comparisons
        if left == right:
            return arr[left], left, comparisons

        third = (right - left) // 3
        mid1, mid2 = left + third, right - third

        comparisons += 1
        if arr[mid1] < arr[mid2]:
            return recursive_search(left, mid2 - 1)
        else:
            return recursive_search(mid1 + 1, right)

    return recursive_search(0, len(arr) - 1)


# 问题6

# 蛮力法
def brute_force_kth_smallest(arr, k):
    comparisons = 0
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            comparisons += 1
            if arr[j] < arr[i]:
                count += 1
        # 确保唯一匹配，处理重复元素
        if count == k - 1:
            return arr[i], comparisons
    return None, comparisons


# 预排序
def sorted_kth_smallest(arr, k):
    comparisons = [0]  # 使用列表封装，便于递增计数

    def custom_sort(x):
        # 模拟比较次数
        comparisons[0] += 1
        return x

    sorted_arr = sorted(arr, key=custom_sort)
    return sorted_arr[k - 1], comparisons[0]


# 减可变规模
def quickselect_kth_smallest(arr, k):
    comparisons = 0

    def partition(low, high):
        nonlocal comparisons
        pivot = arr[high]
        i = low
        for j in range(low, high):
            comparisons += 1
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quickselect(low, high, k):
        nonlocal comparisons
        if low == high:
            return arr[low]
        pivot_index = partition(low, high)
        # 递归过程中的比较次数被隐含在 `partition` 中
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return quickselect(low, pivot_index - 1, k)
        else:
            return quickselect(pivot_index + 1, high, k)

    result = quickselect(0, len(arr) - 1, k - 1)
    return result, comparisons


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 4

    # 蛮力法
    result, comp = brute_force_kth_smallest(arr, k)
    print(f"蛮力法: 第{k}小的元素是 {result}, 比较次数 {comp}")

    # 预排序法
    result, comp = sorted_kth_smallest(arr, k)
    print(f"预排序法: 第{k}小的元素是 {result}, 比较次数 {comp}")

    # 减可变规模法（Quickselect）
    result, comp = quickselect_kth_smallest(arr, k)
    print(f"Quickselect法: 第{k}小的元素是 {result}, 比较次数 {comp}")