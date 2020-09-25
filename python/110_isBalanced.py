"""
110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

date : 9-25-2020
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from python.binaryTree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.isBalanced(root.left) and \
                   self.isBalanced(root.right) and \
                   abs(self.depth(root.left) - self.depth(root.right)) <= 1

    def depth(self, root) -> int:
        if not root:
            return 0
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1


a = TreeNode(None)
a = a.exampleTree()
a.printTree(a)
sol = Solution()


print(sol.isBalanced(a))
