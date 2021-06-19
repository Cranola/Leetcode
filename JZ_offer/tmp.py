# """
# 求解一元多次方程的近似解，误差范围在e-1
# """
#
#
# def find_value(w: list, left: int, right: int):
#     x = left
#     start_offset = 1
#
#     while start_offset > 10 ** (-1):
#         f = 0
#         grad = 0
#         x0 = x
#         new_f = 0
#         for i in range(len(w)):
#             f += w[i] * (x0 ** i)
#             if i > 0:
#                 grad += i * w[i] * (x0 ** (i-1))
#         x = x0 - f/grad
#         for i in range(len(w)):
#             new_f += w[i] * (x ** i)
#         start_offset = abs(new_f - f)
#
#     if left <= x <= right:
#         return x
#     else:
#         print("在指定区间%d到%d内没有符合条件的解" % (left, right))
#
#
# print(find_value([1, 1, 1], -2, 0))
def numberOfDice(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # 为了将index与n对应上，特意把第0行空出来
    res = [[0 for i in range(6*n+1)] for i in range(n+1)]

    # 将第0行与第0列空出来，res[1][1:7] = [1,1,1,1,1,1]
    # 表示第一个骰子6种情况各出现一次
    for i in range(1,7):
        res[1][i] = 1

    # 从第二个骰子开始遍历
    for i in range(2,n+1):
        # n个骰子之和的范围为n到6*n
        for j in range(i, 6*i+1):
            # 当 j > 6 时，f(n) = f(n-1)+f(n-2)+f(n-3)+f(n-4) +f(n-5)+f(n-6)
            # 当 j <= 6 时，例如3，f(n) = f(n-1)+f(n-2)
            for k in range(1, min(j+1,7)):
                res[i][j] += res[i-1][j-k]

    return res

print(numberOfDice(3))

