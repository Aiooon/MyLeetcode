"""
剑指 Offer 35. 复杂链表的复制
请实现 copyRandomList 函数，复制一个复杂链表。
在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
还有一个 random 指针指向链表中的任意节点或者 null。

https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/

date : 1-25-2021
"""

# Definition for a Node.
from typing import List


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        l = []
        node = self.next
        while node:
            l.append(node)
            node = node.next
        return " -> ".join(str(node.val) + ',' + str(node.random) for node in l)


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        dic = {}
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next

        return dic[head]


if __name__ == '__main__':
    nums = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = Node(0)
    cur = head
    for num in nums:
        node = Node(num[0], None, num[1])
        cur.next = node
        cur = cur.next
    # print(head)
    new = Solution().copyRandomList(head)
    print(new)
