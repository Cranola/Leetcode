"""
Description: Given a linked list, find the k(th) listNode starting from the tail of it.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def findKthToTail(head, k):
    if not head or k <= 0:
        return None
    else:
        copy_head = head
        # 首个节点算第一个节点，因此先走k-1步，到达正数第k个节点
        for i in range(k-1):
            # 要考虑倒数第k个节点已经超出链表长度的情况
            if copy_head.next:
                copy_head = copy_head.next
            else:
                return None
        while copy_head.next:
            head = head.next
            copy_head = copy_head.next
        return head.val


if __name__ == "__main__":
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    first.next = second
    second.next = third
    third.next = fourth

    result = findKthToTail(first, 2)
    print(result)