def getDepth(root):
    if not root:
        return 0
    l_depth = getDepth(root.left)
    r_depth = getDepth(root.right)
    return max(l_depth+r_depth) +1


def isBalancedTree(pRoot):
    if not pRoot:
        return True
    if abs(getDepth(pRoot.left) - getDepth(pRoot.right)) > 1:
        return False
    return isBalancedTree(pRoot.left) and isBalancedTree(pRoot.right)
