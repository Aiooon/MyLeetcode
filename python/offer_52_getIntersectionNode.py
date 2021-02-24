"""
剑指 Offer 52. 两个链表的第一个公共节点
输入两个链表，找出它们的第一个公共节点。

示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

date: 2021年2月24日
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 双指针法
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA
        
        return curA

    # 辅助栈法
    def getIntersectionNode_stack(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        stackA, stackB = [], []
        curA, curB = headA, headB
        while curA:
            stackA.append(curA)
            curA = curA.next
        while curB:
            stackB.append(curB)
            curB = curB.next
        node = None
        while stackA and stackB and stackA[-1] == stackB[-1]:
            node = stackA.pop()
            stackB.pop()
        return node

    # 同步法
    def getIntersectionNode_step(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        flag = True if lenA >= lenB else False
        step = lenA-lenB if flag else lenB - lenA
        curA, curB = headA, headB
        if flag:
            while step:
                curA = curA.next
                step -= 1
        else:
            while step:
                curB = curB.next
                step -= 1
        while curA != curB:
            curA = curA.next
            curB = curB.next
        return curA




if __name__ == '__main__':
    pass
