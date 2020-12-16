"""
剑指 Offer 25. 合并两个排序的链表
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000

注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/

date : 12-16-2020
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        newhead = ListNode(0)
        pos, pos1, pos2 = newhead, l1, l2
        while pos1 and pos2:
            if pos1.val <= pos2.val:
                pos.next = pos1
                pos1 = pos1.next
            else:
                pos.next = pos2
                pos2 = pos2.next
            pos = pos.next
        if pos1:
            pos.next = pos1
        if pos2:
            pos.next = pos2
        return newhead.next

if __name__ == '__main__':
    """
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    """
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    newhead = Solution().mergeTwoLists(head1, head2)
    pos = newhead
    while pos:
        print(pos.val)
        pos = pos.next
