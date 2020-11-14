"""
206. 反转链表
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

date : 11-13-2020
"""

# Definition for singly-linked list.
from python.singlyLinkedList import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse_head = None
        while head:
            next = head.next
            head.next = reverse_head
            reverse_head = head
            head = next
        return reverse_head


nums = [1, 2, 3, 4, 5]
head = ListNode().buildList(nums)
head.printList(head)

h = head.reverseList(head)
h.printList(h)
