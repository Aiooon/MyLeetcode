"""
剑指 Offer 22. 链表中倒数第k个节点
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从 1 开始计数，即链表的尾节点是倒数第 1 个节点。
例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。
这个链表的倒数第 3 个节点是值为 4 的节点。

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

date : 12-22-2020
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        nums = []
        cur = self
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return " -> ".join(str(num) for num in nums)


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> Optional[ListNode]:
        if not head:
            return None
        frontNode, backNode = head, head
        while k and frontNode:
            frontNode = frontNode.next
            k -= 1
        while frontNode:
            backNode = backNode.next
            frontNode = frontNode.next

        return backNode


if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        newNode = ListNode(i)
        cur.next = newNode
        cur = cur.next
    print(head)
    print(Solution().getKthFromEnd(head, 1))
    print(Solution().getKthFromEnd(head, 2))
    print(Solution().getKthFromEnd(head, 3))
