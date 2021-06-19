"""
二叉树的前序遍历的递归与非递归写法。
"""
def tra_recursion(root):
    if not root:
        return []
    return [root.val] + tra_recursion(root.left) + tra_recursion(root.right)

def tra_non_recursion(root):
    if not root: return []
    res = []
    stack = [root]
    while stack:
        curr_node = stack.pop()
        if curr_node.right:
            stack.append(curr_node.right)
        if curr_node.left:
            stack.append(curr_node.right)
        res.append(curr_node.val)
    return res
