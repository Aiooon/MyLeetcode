"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]

提示：
链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100

date : 11-6-2020
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def recur_swap(head: ListNode):
    if not head or not head.next:
        return head
    newhead = head.next
    head.next = recur_swap(newhead.next)
    newhead.next = head
    return newhead

def iter_swap(head: ListNode):
    if not head or not head.next:
        return head
    newhead = ListNode()
    newhead.next = head
    temp = newhead
    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next
        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp = node1
    return newhead.next

class Solution:
    # recursive
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        return newhead

    # iteration
    def iter_swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = ListNode()
        newHead.next = head
        temp = newHead
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return newHead.next



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

head = a
while head:
    print(head.val)
    head = head.next
print("------------------")

# new1 = Solution().swapPairs(a)
new2 = Solution().iter_swapPairs(a)
# while new1:
#     print(new1.val)
#     new1 = new1.next

while new2:
    print(new2.val)
    new2 = new2.next


# n = ListNode()
# print(n, n.next, n.val)

