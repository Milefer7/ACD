# 时间限制装饰器
def time_limit(max_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > max_time:
                print(f"计算超时，耗时: {elapsed_time:.2f}秒")

            return result, elapsed_time
        return wrapper
    return decorator