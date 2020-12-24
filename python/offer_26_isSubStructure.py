"""
剑指 Offer 26. 树的子结构
输入两棵二叉树 A和 B，判断 B是不是 A的子结构。(约定空树不是任意一个树的子结构)
B是 A的子结构， 即 A中有出现和 B相同的结构和节点值。
例如:
给定的树 A:
     3
    / \
   4   5
  / \
 1   2

给定的树 B：
   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
  1          3
 / \        /
2   3      1
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
     3          4
    / \        /
   4   5      1
  / \
 1   2
输出：true

限制：0 <= 节点个数 <= 10000

date : 12-23-2020
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        """
        思路：递归 + 回溯
        循环匹配 A 树中的节点和 B 树中的节点，当匹配上时，继续判断左子树和右子树是否相等
        :param A:
        :param B:
        :return:
        """

        def isEqual(node_A: TreeNode, node_B: TreeNode) -> bool:
            # B 树为空说明匹配完成
            if not node_B:
                return True
            # A 为空或当前两个节点的值不相等说明匹配失败
            if not node_A or node_A.val != node_B.val:
                return False
            # 当前节点相同则继续判断两树的左子树和右子树
            return isEqual(node_A.left, node_B.left) and isEqual(node_A.right, node_B.right)
        if not A or not B:
            return False
        return isEqual(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


if __name__ == '__main__':
    """
    输入：A = [3,4,5,1,2], B = [4,1]
         3          4
        / \        /
       4   5      1
      / \
     1   2
    输出：true
    """
    A = TreeNode(3)
    A.left = TreeNode(4)
    A.right = TreeNode(5)
    A.left.left = TreeNode(1)
    A.left.right = TreeNode(2)
    B = TreeNode(4)
    B.left = TreeNode(1)
    print(Solution().isSubStructure(A, B))
