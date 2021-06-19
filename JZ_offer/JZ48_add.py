"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
1,2 ==> 3
"""


def Add(num1, num2):
    # write code here
    # 加进位之后可能还有进位
    pos_sum = num1
    while num2:
        pos_sum = (num1 ^ num2) & 0xffffffff  # 求和
        num2 = ((num1 & num2) << 1) & 0xffffffff  # 求进位
        num1 = pos_sum

    if pos_sum <= 0x7fffffff:
        return pos_sum
    else:
        return ~ (pos_sum ^ 0xffffffff)


print(Add(-3, -7))
