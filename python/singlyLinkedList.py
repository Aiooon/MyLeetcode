# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None

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
    def printList(self, head):
        """

        :param head: head node of the Linked List
        :return: No return
        """
        res = ""
        while head is not None:
            if head.next is not None:
                res = res + str(head.val) + " -> "
            else:
                res = res + str(head.val)
            head = head.next
        print(res)

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

# nums = [1, 2, 3, 4, 5]
# head = ListNode().buildList(nums)
# head.printList(head)
# print(head.length)