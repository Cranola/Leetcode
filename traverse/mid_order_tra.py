"""
二叉树的中序遍历的递归与非递归写法。
"""
def tra_recursion(root):
    if not root: return []
    return tra_recursion(root.left) + [root.val] + tra_recursion(root.right)

def tra_non_recursion(root):
    res, stack = [], []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            curr_node = stack.pop()
            res.append(curr_node.val)
            root = curr_node.right
    return res