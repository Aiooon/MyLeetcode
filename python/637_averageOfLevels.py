"""
637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

示例 1：
输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

提示：节点值的范围在32位有符号整数范围内。
"""
from binaryTree import TreeNode


def averageOfLevels(root: TreeNode):
    """
    :param root: TreeNode
    :return:  List[float]
    """
    def DFS(root: TreeNode, level: int):
        if not root:
            return
        if level < len(totals):    # level < len(totals) means that current level has been watched
            counts[level] += 1
            totals[level] += root.val
        else:
            counts.append(1)
            totals.append(root.val)
        DFS(root.left, level + 1)
        DFS(root.right, level + 1)

    counts = []  # count the node numbers of each level
    totals = []  # count the total sums of each level
    DFS(root, 0)
    return [total / count for total, count in zip(totals, counts)]


A = TreeNode(3)
B = TreeNode(9)
C = TreeNode(20)
D = TreeNode(15)
E = TreeNode(7)
A.left = B
A.right = C
C.left = D
C.right = E
print(averageOfLevels(A))
