"""
剑指offer 08 二叉树的下一个节点
给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？
    3
   / \
  9  20
    /  \
   15   7

inorder : 9 3 15 20 7
input : 15
oupyt : 20

date : 9-23-2020
"""
from python.binaryTree import TreeNode

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
"""


def nextNode(pNode: TreeNode) -> TreeNode:
    noneNode = TreeNode(None)
    if pNode.right:
        tmp = pNode.right
        while tmp.left:
            tmp = tmp.left
        return tmp
    else:
        if pNode.parent.left is pNode:
            return pNode.parent
        else:
            tmp = pNode.parent
            if tmp.parent.left:
                while tmp.parent.left is not tmp:
                    tmp = tmp.parent
                    if not tmp.parent.left:
                        return noneNode
                return tmp
            else:
                return noneNode
    return noneNode


"""
      1
    /   \
   2     3
  / \   / \
 4   5 6   7 

 inorder    : 4251637
"""
noneNode = TreeNode(None)
a1 = TreeNode(1)
b2 = TreeNode(2)
c3 = TreeNode(3)
d4 = TreeNode(4)
e5 = TreeNode(5)
f6 = TreeNode(6)
g7 = TreeNode(7)

a1.left = b2
a1.right = c3
b2.left = d4
b2.right = e5
c3.left = f6
c3.right = g7


a1.parent = noneNode
b2.parent = a1
c3.parent = a1
d4.parent = b2
e5.parent = b2
f6.parent = c3
g7.parent = c3


a1.printTree(a1)
print("Inorder Traversal: ", a1.inorderTraversal(a1))
print("Node {}'s nextNode: {}".format(a1.val, nextNode(a1).val))
print("Node {}'s nextNode: {}".format(b2.val, nextNode(b2).val))
print("Node {}'s nextNode: {}".format(c3.val, nextNode(c3).val))
print("Node {}'s nextNode: {}".format(d4.val, nextNode(d4).val))
print("Node {}'s nextNode: {}".format(e5.val, nextNode(e5).val))
print("Node {}'s nextNode: {}".format(f6.val, nextNode(f6).val))
print("Node {}'s nextNode: {}".format(g7.val, nextNode(g7).val))

