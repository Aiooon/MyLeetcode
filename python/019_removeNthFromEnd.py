"""
19. 删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？

date : 11-17-2020
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from python.singlyLinkedList import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = self.length(head)
        if l == 1 and n == 1:
            return None
        i = 0
        h = head
        while i < l - n:
            h = h.next
            i += 1
        self.removeNode(h, head)
        return head

    def length(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l

    def removeNode(self, node, head):
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        # 删除尾结点
        else:
            h = head
            while h.next.next:
                h = h.next
            h.next = None



nums = [1, 2, 3, 4, 5]
head = ListNode().buildList(nums)
head.printList(head)
Solution().removeNthFromEnd(head, 2)
head.printList(head)

