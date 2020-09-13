"""
257. 二叉树的所有路径
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。

示例:
输入:
   1
 /   \
2     3
 \
  5
输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

date: 9-5-2020
"""

from typing import List

import collections

from binaryTree import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths_DFS(self, root: TreeNode) -> List[str]:
        # DFS
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root,"")
        return paths

    def binaryTreePaths_BFS(self, root: TreeNode) -> List[str]:
        paths = list()
        if not root:
            return paths

        node_queue = collections.deque([root])
        path_queue = collections.deque([str(root.val)])

        while node_queue:
            node = node_queue.popleft()
            path = path_queue.popleft()

            if not node.left and not node.right:
                paths.append(path)
            else:
                if node.left:
                    node_queue.append(node.left)
                    path_queue.append(path + '->' + str(node.left.val))
                if node.right:
                    node_queue.append(node.right)
                    path_queue.append(path + '->' + str(node.right.val))
        return paths

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(5)
A.left = B
A.right = C
B.right = D
s = Solution()
print(s.binaryTreePaths_DFS(A))
print(s.binaryTreePaths_BFS(A))
