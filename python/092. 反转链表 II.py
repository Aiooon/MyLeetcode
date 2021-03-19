"""
92. 反转链表 II
给你单链表的头节点 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

示例 2：
输入：head = [5], left = 1, right = 1
输出：[5]

提示：
链表中节点数目为 n
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

进阶： 你可以使用一趟扫描完成反转吗？

date: 2021年3月18日
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def myprint(self, head):
        nums = []
        if not head:
            return ""
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return " -> ".join(str(num) for num in nums)

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """

        dum_head 记录反转部分的头节点 
        每次都将当前要反转的节点放到头节点前面，并更新头节点为这个节点

        Args:
            head (ListNode): [description]
            left (int): [description]
            right (int): [description]

        Returns:
            ListNode: [description]
        """

        if not head:
            return
        if left == right:
            return head
        dum_head = ListNode()
        dum_head.next = head
        pre = dum_head
        cur = pre.next
        cout_l, cout_r = 1, 1
        while cout_l != left:      # 找到反转部分的左端点
            cout_l += 1
            cout_r += 1
            pre = pre.next
            cur = pre.next
        dum_tail = cur
        cur = cur.next
        cout_r += 1
        while cur and cout_r <= right:
            cout_r += 1
            next_n = cur.next
            cur.next = pre.next
            pre.next = cur
            dum_tail.next = next_n
            cur = next_n
        return dum_head.next


a, b, c, d, e = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
# print(a.myprint(a))
head = Solution().reverseBetween(a, 1, 5)
print(head.myprint(head))