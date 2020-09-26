"""
date : 9-22-2020
test : build binary tree
"""
from python.binaryTree import TreeNode


class CodeforTest:
    def buildTree(self, preorderList, inorderList) -> TreeNode:
        """

        :param preorderList: List[int]
        :param inorderList:  List[int]
        :return: root : TreeNode
        """
        self.preorder = preorderList
        self.inorderDict = {}
        for i in range(len(inorderList)):
            self.inorderDict[inorderList[i]] = i   # 用字典记录每个节点在中序遍历中的位置
        return self.recurProcess(0, 0, len(inorderList) - 1)

    def recurProcess(self, pre_root, in_left, in_right):
        if in_left > in_right:
            return
        root = TreeNode(self.preorder[pre_root])  # 建立当前子树的根节点
        i = self.inorderDict[root.val]
        root.left = self.recurProcess(pre_root + 1, in_left, i - 1)
        root.right = self.recurProcess(i - in_left + pre_root + 1, i + 1, in_right)
        return root


sol = CodeforTest()


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

preorder_ = [3, 9, 8, 5, 10, 20, 15, 7]
inorder_ = [5, 8, 10, 9, 3, 15, 20, 7]

preorder__ = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 7, 13]
inorder__ = [8, 4, 9, 2, 10, 5, 11, 1, 6, 12, 3, 13, 7]


# root = sol.buildTree(preorder, inorder)
# print(root.printTree(root))
#
# root_ = sol.buildTree(preorder_, inorder_)
# print(root_.printTree(root_))
#
# root__ = sol.buildTree(preorder__, inorder__)
# print(root__.printTree(root__))


# 位运算
print(0o10)     # 八进制
print(0x10)     # 十六进制
print(0b10)     # 二进制

x = 0b1010      # 1010  10
y = 1           # 0001   1
print("x = {}, y = {}".format(x, y))
print("x >> y =", x >> y)   # x = 0101      5
print("x << y =", x << y)   # x = 10100     20
print("x & y =", x & y)     # 0000  且操作，返回结果的每一位是 x 和 y 中对应位做 and 运算的结果，只有 1 and 1 = 1，其他情况位0
print("x | y =", x | y)     # 1011  或操作，返回结果的每一位是 x 和 y 中对应位做 or 运算的结果，只有 0 or 0 = 0，其他情况位1
print("~x =", ~x)           # 10101  反转操作，对 x 求的每一位求补，只需记住结果是 -x - 1
print("x ^ y =", x ^ y)     # 1011  或非运算，如果 y 对应位是0，那么结果位取 x 的对应位，如果 y 对应位是1，取 x 对应位的补


