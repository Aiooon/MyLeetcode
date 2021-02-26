"""
剑指 Offer 54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4

限制：1 ≤ k ≤ 二叉搜索树元素个数

date: 2021年2月26日
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # todo 二叉搜索树的中序遍历是递增序列
        # 第 k 大的节点就是倒数第 k 个节点
        # 中序：左根右     倒中序：右根左

        def dfs(root):
            if not root:
                return
            dfs(root.right)
            if self.k == 0:
                return
            self.k -= 1
            if self.k == 0:
                self.res = root.val
            dfs(root.left)
        
        self.k = k
        dfs(root)
        return self.res


a, b, c, d = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
a.right, c.left, c.right = b, a, d
print(Solution().kthLargest(c, 1))