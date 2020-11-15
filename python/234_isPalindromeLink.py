"""
234. 回文链表
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

date : 11-14-2020
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from python.singlyLinkedList import ListNode


class Solution:
    """
    思路（快慢指针）：
    将链表的后半部分反转，然后和前半部分比较，比较完后还原链表（使用该函数的人不希望链表被改变）
    时间复杂度 O(n)  空间复杂度O(1)
    但是这种方法会锁定其他线程对该链表的访问，因为函数执行期间链表会改变。

    具体过程
    1. 找到链表前半部分的尾结点    1 -> 2 -> (3) -> 2 -> 1      1 -> (2) -> 2 -> 1
    2. 反转后半部分链表           1 -> 2 -> (3) -> 1 -> 2      1 -> (2) -> 1 -> 2
    3. 判断是否回文               1 -> 2  对比  1 -> 2        1 -> 2 对比 1 -> 2
    4. 还原后半部分链表
    5. return 结果
    """

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        mid = self.findMid(head)
        right = self.reverseList(mid)
        flag = self.compareList(head, right)
        right = self.reverseList(right)
        mid.next = right.next
        return flag

    def findMid(self, head):
        front, back = head, head
        while back and back.next:
            front = front.next
            back = back.next.next
        return front

    def reverseList(self, head: ListNode):
        reverse_head = None
        while head:
            next = head.next
            head.next = reverse_head
            reverse_head = head
            head = next
        return reverse_head

    def compareList(self, head1, head2):
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True


nums = [1, 2, 3, 4, 5]
nums1 = [1, 2, 3, 2, 1]
nums2 = [1, 2, 2, 1]
nums3 = []

head = ListNode().buildList(nums)
head1 = ListNode().buildList(nums1)
head2 = ListNode().buildList(nums2)
head3 = ListNode().buildList(nums3)

print(nums, Solution().isPalindrome(head))
print(nums1, Solution().isPalindrome(head1))
print(nums2, Solution().isPalindrome(head2))
print(nums3, Solution().isPalindrome(head3))

# head.printList(head)
# print(Solution().findMid(head).val)
# head.printList(head)
# h = head.reverseList(head)
# h.printList(h)
