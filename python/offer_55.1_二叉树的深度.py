"""
剑指 Offer 55 - I. 二叉树的深度
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

date: 2021年2月26日
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # if not root:
        #     return 0
        
        # deep_left = self.maxDepth(root.left)
        # deep_right = self.maxDepth(root.right)

        # return deep_left+1 if deep_left > deep_right else deep_right+1
        if not root: 
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


a,b,c,d,e,f,g = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7) 
a.left, a.right = b, c
b.left, b.right = d, e
c.right = f
e.left = g

print(Solution().maxDepth(a))
