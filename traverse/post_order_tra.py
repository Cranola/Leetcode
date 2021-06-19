"""
二叉树的后序遍历的递归与非递归写法。
"""
def tra_recursion(root):
    if not root: return []
    return tra_recursion(root.left) + tra_recursion(root.right) + []

def tra_non_recursion1(root):
    """
    将正常的遍历序列倒转后发现与前序遍历有很大的相似性。
    """
    if not root: return []
    res, stack = [], [root]
    while stack:
        curr_node = stack.pop()
        res.append(curr_node.val)

        if curr_node.left:
            stack.append(curr_node.left)
        if curr_node.right:
            stack.append(curr_node.right)
    return res[::-1]


def tra_non_recursion2(root):
    """
    常规寻找遍历，插入结果时总是放到最前面。
    """
    res, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            res.insert(0, root.val)
            root = root.right
        else:
            curr_node = stack.pop()
            stack.append(curr_node.left)
    return res
