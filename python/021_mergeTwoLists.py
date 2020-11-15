"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

date : 11-15-2020
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from python.singlyLinkedList import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mergehead = ListNode(-1)
        head = mergehead
        while l1 and l2:
            if l1.val < l2.val:
                mergehead.next = l1
                l1 = l1.next
            else:
                mergehead.next = l2
                l2 = l2.next
            mergehead = mergehead.next
        mergehead.next = l1 if l1 else l2
        return head.next


nums1 = [1, 3]
nums2 = [2]
l1 = ListNode().buildList(nums1)
l2 = ListNode().buildList(nums2)
l1.printList(l1)
l2.printList(l2)
merge = Solution().mergeTwoLists(l1, l2)
merge.printList(merge)

