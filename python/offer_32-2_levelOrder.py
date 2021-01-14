"""
剑指 Offer 32 - II. 从上到下打印二叉树 II
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]

提示：
节点总数 <= 1000
注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

date : 1-14-2020
"""

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        seq = []
        queue = [root]
        while queue:
            lay_seq = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                lay_seq.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            seq.append(lay_seq)
        return seq


if __name__ == '__main__':
    root = TreeNode(3)
    a, b, c, d = TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
    root.left, root.right = a, b
    b.left, b.right = c, d
    print(Solution().levelOrder(root))
