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


root = sol.buildTree(preorder, inorder)
print(root.printTree(root))

root_ = sol.buildTree(preorder_, inorder_)
print(root_.printTree(root_))

root__ = sol.buildTree(preorder__, inorder__)
print(root__.printTree(root__))


