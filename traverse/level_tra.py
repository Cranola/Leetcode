"""
二叉树的层次遍历。any()函数判断可迭代形参中元素是否全部为空。
"""
def binary_level_tra(root):
    if not root: return []
    res, stack = [], [root]
    while stack:
        res.append([node.val for node in stack])
        stack = [kid for node in stack for kid in (node.left, node.right) if kid]
    return res

"""
多叉树的层次遍历。
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

def multi_level_tra(root):
    if not root: return []
    res, stack = [], [root]
    while stack:
        res.append([node.val for node in stack])
        stack = [kid for node in stack for kid in node.children if kid]
    return res
