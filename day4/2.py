# #########递归计算阶乘
# def fun_one(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fun_one(n-1)
#
# num = int(input("请输入一个数据,将要计算他的阶乘"))
# print(f"{num}的阶乘是:{fun_one(num)}")


def fibonacci_list(n):
    """

    :param n:
    :return:生成前 n 项斐波那契数列
    """

    if n <= 0:
        return []
    if n == 1:
        return [1]

    result = [1, 1]
    for i in range(2, n):
        result.append(result[-1] + result[-2])  # 前两项相加
    return result


print(fibonacci_list(10))

def fibonacci(n):
    """

    :param n:
    :return: 返回斐波那契数列第N个数字
    """
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # 5（数列：1,1,2,3,5）