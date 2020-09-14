# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # create tree with list (not finish)
    def createTreeWithList(self, root, llist, i):
        """
        :param list:
        :param index:
        :return:
        """
        if i < len(llist):
            if llist[i] == '#':
                return None  ###这里的return很重要
            else:
                root = TreeNode(llist[i])
                # print('列表序号：' + str(i) + ' 二叉树的值：' + str(root.val))# 往左递推
                root.left = self.createTreeWithList(root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空， # 往右回溯
                root.right = self.createTreeWithList(root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右， # 再返回根'
                # print('************返回根：', root.val)
                return root  ###这里的return很重要
        return root

    # print binary tree with tree structure (not finish)
    def function(self, root):
        A = []
        result = []
        if not root:
            return result
        A.append(root)
        while A:
            current_root = A.pop(0)
            result.append(current_root.val)
            if current_root.left:
                A.append(current_root.left)
            if current_root.right:
                A.append(current_root.right)
        return result

    # Non-recursive preorder traversal
    def preorderTraversal(self, root):
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
                seq.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return seq

    # Non-recursive inorder traversal
    def inorderTraversal(self, root):
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

    # Non-recursive postorder traversal
    # 把先序顺序中的 ‘根左右’ 转换为 ‘根右左’，然后反过来就变成了‘左右根’。
    def postorderTraversal(self, root):
        """

        :param root:
        :return:
        """
        if root is None:
            return []

        seq = []
        stack = []
        output = []
        while root or len(stack) != 0:
            if root:
                seq.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                root = root.left

        while seq:
            output.append(seq.pop())

        return output

    def layerorderTraversal(self, root):
        """

        :param root:
        :return:
        """
        if root is None:
            return []

        seq = []
        queue = []
        queue.append(root)
        while queue:
            root = queue.pop(0)
            seq.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return seq

# llist = [1, 2, 3, 4, 5]
# A = TreeNode(1)
# A.createTreeWithList(None, llist, 0)
# print(A.function(A))

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

"""
      1
    /   \
   2     3
  / \   / \
 4   5 6   7 
 preorder   : 1245367
 inorder    : 4251637
 postorder  : 4526731
 layerorder : 1234567
"""


print("preorder Traversal: ", a.preorderTraversal(a))
print("inorder Traversal: ", a.inorderTraversal(a))
print("postorder Traversal: ", a.postorderTraversal(a))
print("layerorder Traversal: ", a.layerorderTraversal(a))
