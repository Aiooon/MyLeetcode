"""
剑指 Offer 06. 从尾到头打印链表

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]

限制:0 <= 链表长度 <= 10000

date:9-5-2020
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

from python.singlyLinkedList import ListNode


def reversePrint(head: ListNode) -> List[int]:
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    return stack[::-1]


def reversePrint_recursive(head: ListNode) -> List[int]:
    return reversePrint_recursive(head.next) + [head.val] if head else []


A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(5)

A.next = B
B.next = C
C.next = D
print(reversePrint(A))


