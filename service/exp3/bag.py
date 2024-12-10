def greedy_fractional(capacity, items):
    max_value = 0
    initial_capacity = capacity  # 保存初始容量
    # 根据物品的价值密度（价值 / 重量）进行排序，降序排列
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    # 打印表头
    print(f"{'物品':<10}{'价值':<12}{'重量':<12}{'选择比例':<12}{'累计价值':<12}{'剩余容量':<12}")
    print("-" * 60)

    for item in items:
        if capacity == 0:
            break  # 背包已经满了

        if item[1] <= capacity:  # 如果物品可以完全放入
            max_value += item[0]
            capacity -= item[1]
            fraction = 1  # 全部放入
        else:
            # 只能放入部分物品
            fraction = capacity / item[1]  # 选择的比例
            max_value += item[0] * fraction
            capacity = 0  # 背包容量用完

        # 打印当前物品的选择信息
        print(f"{str(item):<10}{item[0]:<10}{item[1]:<10}{fraction:<10.2f}{max_value:<10.2f}{capacity:<10}")

    print("-" * 60)
    print(f"最大价值: {max_value}, 最终背包重量: {initial_capacity - capacity}")
    return max_value, initial_capacity - capacity  # 返回最大价值和最终背包重量


# 问题 3: 贪心算法解决0-1背包问题（近似解）
def greedy_01(capacity, items):
    # 根据物品的价值密度（价值 / 重量）进行排序，降序排列
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    max_value, max_weight = 0, 0

    # 打印表头
    print(f"{'物品':<10}{'价值':<10}{'重量':<10}{'选择':<12}{'累计价值':<12}{'背包重量':<12}")
    print("-" * 60)

    # 遍历物品，进行选择
    for item in items:
        # 判断物品是否可以放入背包
        if max_weight + item[1] <= capacity:  # 如果物品可以完全放入背包
            max_value += item[0]
            max_weight += item[1]
            selected = "是"  # 物品被放入背包
        else:
            selected = "否"  # 物品未放入背包

        # 打印当前物品的选择情况
        print(f"{str(item):<10}{item[0]:<10}{item[1]:<10}{selected:<12}{max_value:<12}{max_weight:<12}")

    print("-" * 60)
    print(f"最大价值: {max_value}, 最终背包重量: {max_weight}")

    return max_value, max_weight  # 返回近似解


# 问题 4: 蛮力法解决0-1背包问题（最优解）
def brute_01(capacity, items):
    n = len(items)
    max_value, max_weight = 0, 0
    # 遍历所有可能的组合
    for i in range(1 << n):  # i表示遍历总数
        total_value, total_weight = 0, 0
        combination = []
        for j in range(n):
            # 检查第j个物品是否被选中
            if i & (1 << j):  # 检查第j位是否为1，看看是否选中该物品
                total_value += items[j][0]
                total_weight += items[j][1]
                combination.append(1)
            else:
                combination.append(0)
        # 打印当前组合及其总价值和总重量
        print(f'组合: {combination}, 总价值: {total_value}, 总重量: {total_weight}')
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

    # 打印初始状态
    print(f"{'物品':<10}{'容量':<10}{'选择':<12}{'累计价值':<12}{'累计重量':<12}")
    print("-" * 60)

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # 当前物品的价值和重量
            item_value, item_weight = items[i - 1]

            # 如果选择当前物品，计算新的总价值
            if item_weight <= j:
                total_value = dp_v[i - 1][j - item_weight] + item_value
            else:
                total_value = 0

            # 选择当前物品与不选择当前物品的比较
            if total_value > dp_v[i - 1][j]:  # 如果选择当前物品更优
                dp_v[i][j] = total_value
                dp_w[i][j] = dp_w[i - 1][j - item_weight] + item_weight
                selected = "选"
            else:  # 否则不选择当前物品
                dp_v[i][j] = dp_v[i - 1][j]
                dp_w[i][j] = dp_w[i - 1][j]
                selected = "不选"

            # 打印当前物品的状态
            print(f"物品{i:<2} ({item_value:<3},{item_weight:<3}) | 容量{j:<3} | 选择: {selected:<6} | "
                  f"累计价值: {dp_v[i][j]:<12} | 累计重量: {dp_w[i][j]:<12}")

    # 返回最大价值和重量
    return dp_v[n][capacity], dp_w[n][capacity]  # 返回最大价值和对应的重量


# 问题 6: 动态规划（记忆化搜索优化）
def dynamic_memory_01(capacity, items):
    n = len(items)
    memo = {}  # 记忆化字典，用于存储已经计算过的结果

    def _knapsack(i, remain_capacity):
        # 递归终止条件：物品超出范围或剩余容量为0
        if i >= n or remain_capacity <= 0:
            return 0, 0  # 返回 0价值，0重量

        # 如果已经计算过该子问题，直接返回
        if (i, remain_capacity) in memo:
            return memo[(i, remain_capacity)]

        # 打印当前状态：物品索引、剩余容量
        print(f"考虑物品 {i + 1} (价值: {items[i][0]}, 重量: {items[i][1]})，剩余容量: {remain_capacity}")

        # 不选择当前物品
        not_taken = _knapsack(i + 1, remain_capacity)

        # 选择当前物品（如果可以放入背包）
        taken = 0, 0
        if items[i][1] <= remain_capacity:
            tmp = _knapsack(i + 1, remain_capacity - items[i][1])
            taken = items[i][0] + tmp[0], items[i][1] + tmp[1]

        # 比较选择当前物品和不选择当前物品的结果，选择最大值
        result = max(not_taken, taken, key=lambda item: item[0])

        # 存储结果并返回
        memo[(i, remain_capacity)] = result

        # 打印选择物品后的结果
        print(f"选择物品 {i + 1} 后的最大价值: {result[0]}, 背包总重量: {result[1]}")

        return result

    # 打印表头
    print(f"{'物品':<10}{'价值':<10}{'重量':<10}{'选择':<12}{'累计价值':<12}{'背包重量':<12}")
    print("-" * 60)

    # 从第一个物品开始，剩余容量为 `capacity`
    max_value, total_weight = _knapsack(0, capacity)

    print("-" * 60)
    print(f"最大价值: {max_value}, 最终背包重量: {total_weight}")

    return max_value, total_weight  # 返回最大价值和最终背包重量
