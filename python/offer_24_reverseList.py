"""
剑指 Offer 24. 反转链表
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

限制：
0 <= 节点个数 <= 5000

注意：本题与主站 206 题相同：https://leetcode-cn.com/problems/reverse-linked-list/

date : 12-22-2020
"""
# Definition for singly-linked list.
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
    def reverseList(self, head: ListNode) -> ListNode:
        newHead = None
        cur = head
        while cur:
            newNode = ListNode(cur.val)
            newNode.next = newHead
            newHead = newNode
            cur = cur.next
        return newHead


if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        newNode = ListNode(i)
        cur.next = newNode
        cur = cur.next
    print(head)
    print(Solution().reverseList(head))