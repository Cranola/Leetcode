def find_couple_fixed_sum(array, c):
    if len(array) < 2:
        return None
    res = []
    left, right = 0, len(array)-1
    while left < right:
        if array[left] + array[right] == c:
            res.append([array[left], array[right]])
            # 检查会不会有死循环
            left += 1
            right -= 1
        elif array[left] + array[right] < c:
            left += 1
        else:
            right -= 1
    if len(res) == 0:
        return None
    res_index = 0
    curr_value = float('inf')
    for i in range(len(res)):
        value = res[i][0] * res[i][1]
        if value < curr_value:
            curr_value = value
            res_index = i
    return res[res_index]


print(find_couple_fixed_sum([1,2,3,4,5,6,7], 7))

