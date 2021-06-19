"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时
包含指向父结点的指针。
"""


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        while pNode.next:
            p = pNode.next
            if p.left == pNode:
                return p
            pNode=p
