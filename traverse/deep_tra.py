"""
树的深度遍历。
"""
def deep_tra(root):
    if not root: return
    print(root.val)
    deep_tra(root.left)
    deep_tra(root.right)