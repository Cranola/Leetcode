def string_to_int(s):
    # 特殊情况判断
    if len(s) == 0:
        return 0
    res = 0
    place = 0
    flag = 1
    # 判断符号
    if s[0] in '+-':
        if s[0] == '-':
            flag = -1
        s = s[1:]
    # 从后往前计算
    for i in range(len(s)-1, -1, -1):
        # 0的ASCII码值为48
        if ord(s[i])-48 > 9 or ord(s[i])-48 < 0:
            return 0
        else:
            res += (ord(s[i])-48)*(10**place)
            place += 1
    return res * flag


print(string_to_int('-12345'))

