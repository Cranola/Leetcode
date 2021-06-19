"""
有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。每个孩子只能吃最多一个饼干，且只有饼干的
大小大于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩子可以吃饱。
"""


def candy_allocation(children: list, candy: list):
    children.sort()
    candy.sort()
    child = 0
    candy_num = 0
    while (child < len(children)) and (candy_num < len(candy)):
        if children[child] <= candy[candy_num]:
            child += 1
        candy_num += 1
    return child


full_children_num = candy_allocation([1, 2, 3], [1, 2])
print(full_children_num)

"""
一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，规则是如果一个孩子的评分比自己身旁的
一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果；所有孩子至少要有一个糖果。求解最少需要多少个糖果
"""


def weight_children_allocation(children: list):
    candy = [1] * len(children)
    for i in range(1, len(children)):
        if children[i] > children[i-1]:
            candy[i] += 1

    for j in range(len(children)-2, -1, -1):
        if children[j] > children[j+1]:
            candy[j] += 1
    return sum(candy)


need_candy = weight_children_allocation([1, 0, 2])
print(need_candy)