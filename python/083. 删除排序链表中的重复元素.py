"""
83. 删除排序链表中的重复元素
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：
链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列

date: 2021年3月26日
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dum_head = ListNode(-1, head)
        cur = dum_head.next
        while cur:
            next_n = cur.next
            if not next_n: break
            if cur.val == next_n.val:
                while next_n and cur.val == next_n.val:
                    next_n = next_n.next
                cur.next = next_n
            else:
                cur = cur.next
        return dum_head.next

