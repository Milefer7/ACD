# 问题 2: 贪心算法解决分数背包问题
def greedy_fractional(capacity, items):
    max_value, max_weight = 0, capacity
    # 根据物品的价值密度（价值 / 重量）进行排序，降序排列
    sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    for item in items:
        if capacity == 0:
            break  # 背包已经满了
        if item[1] <= capacity:
            max_value += item[0]  # 如果物品完全放得下，放入背包
            capacity -= item[1]  # 减少剩余容量
        else:
            max_value += (item[0] / item[1]) * capacity  # 放入部分物品
            capacity = 0  # 背包容量用完
    return max_value, max_weight  # 返回最大价值和最终背包重量


# 问题 3: 贪心算法解决0-1背包问题（近似解）
def greedy_01(capacity, items):
    # 根据物品的价值密度（价值 / 重量）进行排序，降序排列
    sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    max_value, max_weight = 0, 0
    for item in items:
        if max_weight + item[1] <= capacity:  # 如果物品可以完全放入背包
            max_value += item[0]
            max_weight += item[1]
    return max_value, max_weight  # 返回近似解


# 问题 4: 蛮力法解决0-1背包问题（最优解）
def brute_01(capacity, items):
    n = len(items)
    max_value, max_weight = 0, 0
    # 遍历所有可能的组合
    for i in range(1 << n):  # 1 << n 是生成所有子集的方式
        total_value, total_weight = 0, 0
        for j in range(n):
            # 检查第j个物品是否被选中
            if i & (1 << j):
                total_value += items[j][0]
                total_weight += items[j][1]
        # 如果未超出容量且总价值大于当前最大值，则更新
        if total_weight <= capacity and max_value < total_value:
            max_value = total_value
            max_weight = total_weight
    return max_value, max_weight  # 返回最大价值和重量


# 问题 5: 动态规划解决0-1背包问题（最优解）
def dynamic_01(capacity, items):
    n = len(items)
    dp_v = [[0] * (capacity + 1) for _ in range(n + 1)]  # dpV[i][j]表示前i个物品放入容量为j的背包的最大价值
    dp_w = [[0] * (capacity + 1) for _ in range(n + 1)]  # dpW[i][j]表示前i个物品放入容量为j的背包的对应总重量
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            total_value = dp_v[i - 1][j - items[i - 1][1]] + items[i - 1][0]  # 如果选择当前物品
            if items[i - 1][1] <= j and dp_v[i - 1][j] < total_value:  # 如果能放入背包且比不选更好
                dp_v[i][j] = total_value
                dp_w[i][j] = dp_w[i - 1][j - items[i - 1][1]] + items[i - 1][1]
            else:
                dp_v[i][j] = dp_v[i - 1][j]  # 不选当前物品
                dp_w[i][j] = dp_w[i - 1][j]
    return dp_v[n][capacity], dp_w[n][capacity]  # 返回最大价值和重量


# 问题 6: 改进的动态规划（使用一维数组减少空间复杂度）
def dynamic_improve_01(capacity, items):
    n = len(items)
    dp_v = [0] * (capacity + 1)  # 一维数组，记录背包容量每个位置的最大价值
    dp_w = [0] * (capacity + 1)  # 一维数组，记录对应的总重量
    for i in range(n):
        for j in range(capacity, items[i][1] - 1, -1):  # 逆向遍历，避免覆盖
            total_value = dp_v[j - items[i][1]] + items[i][0]  # 如果选择当前物品
            if dp_v[j] < total_value:  # 如果选择当前物品后价值更大
                dp_v[j] = total_value
                dp_w[j] = dp_w[j - items[i][1]] + items[i][1]
    return dp_v[capacity], dp_w[capacity]  # 返回最大价值和重量


# 问题 7: 动态规划（记忆化搜索优化）
def dynamic_memory_01(capacity, items):
    n = len(items)
    memo = {}  # 记忆化字典，用于存储已经计算过的结果

    def _knapsack(i, remain_capacity, items):
        # 递归终止条件：物品超出范围或剩余容量为0
        if i >= n or remain_capacity <= 0:
            return 0, 0
        # 如果已经计算过该子问题，直接返回
        if (i, remain_capacity) in memo:
            return memo[(i, remain_capacity)]

        # 不选择当前物品
        not_taken = _knapsack(i + 1, remain_capacity, items)

        # 选择当前物品（如果可以放入背包）
        taken = 0, 0
        if items[i][1] <= remain_capacity:
            tmp = _knapsack(i + 1, remain_capacity - items[i][1], items)
            taken = items[i][0] + tmp[0], items[i][1] + tmp[1]

        # 存储结果并返回最大值
        memo[(i, remain_capacity)] = max(not_taken, taken, key=lambda item: item[0])
        return memo[(i, remain_capacity)]

    return _knapsack(0, capacity, items)  # 调用递归函数，开始背包问题求解
