"""
剑指 Offer 27. 二叉树的镜像
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：
     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

限制： 0 <= 节点个数 <= 1000
注意：本题与主站 226 题相同

date : 1-13-2020
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        """
        思路：
        先根遍历二叉树，交换左右节点
        :param root:
        :return:
        """
        if not root:
            return None
        left = self.mirrorTree(root.right)
        right = self.mirrorTree(root.left)
        root.left = left
        root.right = right
        return root