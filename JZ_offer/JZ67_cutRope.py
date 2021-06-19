"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为
k[1],...,k[m]。请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分
别为2、3、3的三段，此时得到的最大乘积是18。输入一个数n，意义见题面。（2 <= n <= 60）。输出答案。
8 ==> 18
"""


def cutRope(number):
    # 当接近均匀分布的时候，乘积最大
    max_multiply = 0
    for m in range(2, number+1):
        partition = number//m
        residual = number%m
        curr_value = ((partition+1)**residual)*(partition**(m-residual))
        if curr_value > max_multiply:
            max_multiply = curr_value
    return max_multiply


print(cutRope(8))
