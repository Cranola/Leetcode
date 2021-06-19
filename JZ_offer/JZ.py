class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left
        # 连接根与左子树最大节点
        if left:
            while (left.right):
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree

        # 右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right
        # 连接根与右子树最小节点
        if right:
            while(right.left):
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree

        while(pRootOfTree.left):
            pRootOfTree = pRootOfTree.left

        return pRootOfTree