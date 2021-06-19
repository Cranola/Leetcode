def find_first_common_node(pHead1, pHead2):
    # 有链表为空，返回空
    if not pHead1 or not pHead2:
        return None

    # 计算两个链表的长度差
    up = pHead1
    down = pHead2
    while up and down:
        up = up.next
        down = down.next
    # up先走完
    if not up:
        length = 0
        while down:
            down = down.next
            length += 1
        up = pHead1
        down = pHead2
        while length:
            down = down.next
            length -= 1
        while up and down:
            if up == down:
                return up
        return None
    # down先走完
    if not down:
        length = 0
        while up:
            up = up.next
            length += 1
        up = pHead1
        down = pHead2
        while length:
            up = up.next
            length -= 1
        while up and down:
            if up == down:
                return up
        return None

