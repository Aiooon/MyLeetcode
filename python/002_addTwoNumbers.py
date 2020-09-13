# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        cur = fakeHead = ListNode(0)
        carry = 0
        while p or q:
            sum = carry
            if p:
                sum += p.val
                p = p.next
            if q:
                sum += q.val
                q = q.next
            carry = sum / 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
        if carry == 1:
            cur.next = ListNode(carry)
        return fakeHead.next

    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        lastnode = prenode = ListNode(0)
        val = 0
        while val or l1 or l2:
            val, cur = divmod(val + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            '''
            python divmod() 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
            >>> divmod(7, 2)
            (3, 1)
            >>> divmod(8, 2)
            (4, 0)
            >>> divmod(1 + 2j, 1 + 0.5j)
            ((1 + 0j), 1.5j)
            '''
            lastnode.next = ListNode(cur)
            lastnode = lastnode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return prenode.next

def generateList(l: ListNode) -> ListNode:
    lastNode = preNode = ListNode(0)
    for val in l:
        lastNode.next = ListNode(val)
        lastNode = lastNode.next
    return preNode.next

def printList(l:ListNode):
    while l:
        print("%d, " %(l.val), end = '')
        l = l.next
    print(' ')

if __name__ == "__main__":
    l1 = generateList([2, 4, 3])
    l2 = generateList([5, 6, 4])
    printList(l1)
    printList(l2)
    s = Solution()
    sum1 = s.addTwoNumbers(l1, l2)
    sum2 = s.addTwoNumbers_2(l1, l2)
    printList(sum1)
    printList(sum2)