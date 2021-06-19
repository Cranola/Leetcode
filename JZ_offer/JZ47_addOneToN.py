"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
5 ==> 15
"""


def Sum_Solution(n):
    # write code here
    # 利用and的特殊性，a and b, a和b均为真返回b, a真b假返回b, a假b真返回a
    res = n and (n + Sum_Solution(n-1))
    return res