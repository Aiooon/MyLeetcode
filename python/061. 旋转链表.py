"""
61. 旋转链表
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

date: 2021年3月27日
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        快慢指针法

        Args:
            head (ListNode): [description]
            k (int): [description]

        Returns:
            ListNode: [description]
        """
        if not head or not head.next or k == 0:
            return head
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        k %= l
        if k == 0:
            return head
        slow, fast = head, head
        while k:
            fast = fast.next
            k -= 1
        # 此时 slow 和 fast 之间的距离是 k；fast 指向第 k+1 个节点
        # 当 fast.next 为 None 时，fast指向链表最后一个节点，slow指向倒数第 k+1 个节点
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head