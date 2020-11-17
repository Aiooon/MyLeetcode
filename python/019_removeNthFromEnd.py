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
        """
        思路：
        根据链表长度 l，找到第 l-n 个结点，删除下一个结点
        时间复杂度 O(n)
        空间复杂度 O(1)

        :param head:
        :param n:
        :return:
        """
        def length(head):
            l = 0
            while head:
                l += 1
                head = head.next
            return l

        l = length(head)
        dummyhead = ListNode(0, head)
        cur = dummyhead
        for i in range(l-n):
            cur = cur.next
        cur.next = cur.next.next
        return dummyhead.next

    def removeNthFromEndOnce(self, head: ListNode, n: int) -> ListNode:
        """
        思路：只扫描一次的方法
        用前后两个指针，后面的指针比前面的指针超前 n 个结点。同时开始遍历，当后面的指针到达表尾（空）时，
        前一个结点指向的就是倒数第 n 个结点。
        为使删除结点更方便，引入 dummy，sec指向倒数第 n 个结点的前一个结点
        1 -> 2 -> 3 -> 4 -> 5 ->
                  ↑              ↑
                 sec            fst
        初始时：
         dummy -> 1 -> 2 -> 3 -> 4 -> 5 ->
           ↑                ↑
          sec              fst

        :param head:
        :param n:
        :return:
        """
        dummyhead = ListNode(0, head)
        sec = dummyhead
        fst = head
        for i in range(n):
            fst = fst.next
        while fst:
            sec = sec.next
            fst = fst.next
        sec.next = sec.next.next
        return dummyhead.next


nums = [1, 2, 3, 4, 5]
head = ListNode().buildList(nums)
head.printList(head)
Solution().removeNthFromEndOnce(head, 2)
head.printList(head)

