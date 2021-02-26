"""
剑指 Offer 55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

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

限制：0 <= 树的结点个数 <= 10000

date: 2021年2月26日
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return 0
            deep_left = dfs(root.left)
            if deep_left == -1:
                return -1
            deep_right = dfs(root.right)
            if deep_right == -1:
                return -1

            if abs(deep_left - deep_right) <= 1:
                return max(deep_left, deep_right) + 1
            else:
                return -1
                
        return True if dfs(root) != -1 else False


a,b,c,d,e,f,g = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7) 
a.left, a.right = b, c
b.left, b.right = d, e
c.right = f
e.left = g

print(Solution().isBalanced(a))
