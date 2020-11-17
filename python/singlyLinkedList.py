# Definition for singly-linked list.
from typing import List


class ListNode:
    """单链表结构的 Node节点"""
    def __init__(self, val=0, next_node=None):
        """
        Node节点的初始化方法
        :param val: 存储的数据
        :param next_node: 下一个Node节点的引用地址
        """
        self.val = val
        self.next = next_node

    # @property
    # def val(self):
    #     """
    #     Node节点存储数据的获取.
    #     返回: 当前Node节点存储的数据
    #     """
    #     return self.val
    #
    # @val.setter
    # def val(self, val):
    #     """Node节点存储数据的设置方法.
    #     参数:
    #         data:新的存储数据
    #     """
    #     self.val = val
    #
    # @property
    # def next_node(self):
    #     """获取Node节点的next指针值.
    #     返回:
    #         next指针数据
    #     """
    #     return self.next
    #
    # @next_node.setter
    # def next_node(self, next_node):
    #     """Node节点next指针的修改方法.
    #     参数:
    #         next:新的下一个Node节点的引用
    #     """
    #     self.next = next_node

    # Build Singly Linked List with int List
    def buildList(self, nums: List):
        """

        :param nums: input int list to build Singly Linked List
        :return: head of the built Singly Linked List
        """
        head = ListNode(0)
        head_point = head
        for i in range(len(nums)):
            node = ListNode(nums[i])
            head.next = node
            head = head.next
        return head_point.next

    # Format printout linked list
    # def printList(self, head):
    #     """
    #
    #     :param head: head node of the Linked List
    #     :return: No return
    #     """
    #     nums = []
    #     pos = head
    #     while pos:
    #         nums.append(pos.val)
    #         pos = pos.next
    #     print(" -> ".join(str(num) for num in nums))

    # 打印链表
    def __repr__(self) -> str:
        nums = []
        pos = head
        while pos:
            nums.append(pos.val)
            pos = pos.next
        return " -> ".join(str(num) for num in nums)

    # Reverse Linked List
    def reverseList(self, head):
        """

        :param head: head node of the Linked List
        :return: new head
        """
        reverse_head = None
        while head:
            next = head.next
            head.next = reverse_head
            reverse_head = head
            head = next
        return reverse_head

    # Length of Linked List
    def length(self, head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l


nums = [1, 2, 3, 4, 5]
head = ListNode().buildList(nums)
print(head)
print(head.length(head))
