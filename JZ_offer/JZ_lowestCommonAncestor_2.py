class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

n_3 = TreeNode(3)
n_5 = TreeNode(5)
n_1 = TreeNode(1)
n_6 = TreeNode(6)
n_2 = TreeNode(2)
n_0 = TreeNode(0)
n_8 = TreeNode(8)
n_7 = TreeNode(7)
n_4 = TreeNode(4)

n_3.left, n_3.right = n_5, n_1
n_5.left, n_5.right = n_6, n_2
n_1.left, n_1.right = n_0, n_8
n_2.left, n_2.right = n_7, n_4


class Solution:
    def __init__(self):
        self.path_p = None
        self.path_q = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        根据节点路径找最近邻祖先
        :param root:
        :param p:
        :param q:
        :return:
        """
        self.search(root, [], p.val, q.val)
        curr_node = root.val
        for i in range(1, min(len(self.path_p), len(self.path_q))):
            if self.path_p[i] == self.path_q[i]:
                curr_node = self.path_p[i]
            else:
                break
        return curr_node

    def search(self, root, path, p, q):
        """
        找到点p和q在树中的路径
        :param root:
        :param path:
        :param p:
        :param q:
        :return:
        """
        # 终止条件
        if root and root.val == p:
            self.path_p = path + [root.val]
        elif root and root.val == q:
            self.path_q = path + [root.val]

        path.append(root.val)
        if root.left:
            path = self.search(root.left, path, p, q)

        if root.right:
            path = self.search(root.right, path, p, q)
        path.pop()
        return path

test = Solution()
res = test.lowestCommonAncestor(n_3, n_6, n_8)
print(res)


