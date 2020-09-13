# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def preorderTraverse(self):
        if self:
            print(self.val)
            if self.left:
                self.left.preTraverse()
            if self.right:
                self.right.preTraverse()

    def inorderTraverse(self):
        if self:
            if self.left:
                self.left.inorderTraverse()
            print(self.val)
            if self.right:
                self.right.inorderTraverse()

    def postorderTravse(self):
        if self:
            if self.left:
                self.left.inorderTraverse()
            if self.right:
                self.right.inorderTraverse()
            print(self.val)

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:       #非递归
        res = []
        if not root:
            return res
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res

    def preorderTraversal(self, root:TreeNode) -> list(int):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def postorderTraversal(self, root:TreeNode) -> list(int):
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]
