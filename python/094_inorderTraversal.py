"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
date : 9-14-2020
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from python.binaryTree import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """

        :param root:
        :return:
        """
        if root is None:
            return []

        seq = []
        stack = []
        while root is not None or len(stack) != 0:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                seq.append(root.val)  # left child pop first, then root
                root = root.right
        return seq
