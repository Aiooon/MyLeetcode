"""
剑指 Offer 36. 二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
要求不能创建任何新的节点，只能调整树中节点指针的指向。

为了让您更好地理解问题，以下面的二叉搜索树为例：


我们希望将这个二叉搜索树转化为双向循环链表。
链表中的每个节点都有一个前驱和后继指针。
对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。


特别地，我们希望可以就地完成转换操作。
当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。
还需要返回链表中的第一个节点的指针。

注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

date : 1-26-2021
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self):
    #     nums = []
    #
    #     def dfs(node: Node):
    #         if not node:
    #             return
    #         nums.append(node.val)
    #         dfs(node.left)
    #         dfs(node.right)
    #     dfs(self)
    #     return " -> ".join(str(num) for num in nums)


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':

        def dfs(cur: Node):
            if not cur:
                return
            dfs(cur.left)
            if not self.pre:
                self.head = cur
            else:
                self.pre.right, cur.left = cur, self.pre
            self.pre = cur
            dfs(cur.right)

        if not root:
            return None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__ == '__main__':
    a, b, c, d, e = Node(1), Node(2), Node(3), Node(4), Node(5)
    b.left, b.right = a, c
    d.left, d.right = b, e
    # print(d)

    Solution().treeToDoublyList(d)
    print(a.left.val, a.right.val)
    print(b.left.val, b.right.val)
    print(c.left.val, c.right.val)
    print(d.left.val, d.right.val)
    print(e.left.val, e.right.val)


