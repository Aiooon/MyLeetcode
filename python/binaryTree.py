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

    # print Tree in layer order
    def printTreebyLayer(self, root):
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

    def listcreattree(self, root, llist, i):  # 用列表递归创建二叉树，
        # 它其实创建过程也是从根开始a开始，创左子树b，再创b的左子树，如果b的左子树为空，返回none。
        # 再接着创建b的右子树，
        if i < len(llist):
            if llist[i] == '#':
                return None  # 这里的return很重要
            else:
                root = TreeNode(llist[i])
                # 往左递推
                root.left = self.listcreattree(
                    root.left, llist, 2 * i + 1)  # 从根开始一直到最左，直至为空，
                # 往右回溯
                root.right = self.listcreattree(
                    root.right, llist, 2 * i + 2)  # 再返回上一个根，回溯右，
                # 再返回根'
                return root  # 这里的return很重要
        return root

    # 打印为树状图
    def toTree4(self, t):
        n = len(t) - 1
        for i in range(1, n - 1):
            for j in range(2 * i):
                if t[i][j] == '.':
                    t[i + 1].insert(j + 1, '.')
                    t[i + 1].insert(j + 1, '.')
        result = []
        result.append('       {}       '.format(t[0][0]))
        result.append('    /     \\    ')
        result.append('   {}       {}   '.format(t[1][0], t[1][1]))
        result.append('  / \\     / \\  ')
        result.append(' {}   {}   {}   {} '.format(*t[2]))
        result.append('/ \\ / \\ / \\ / \\')
        result.append(' '.join([str(i) for i in t[3]]))
        for i in result[:2 * n - 1]:
            print(i)

    # 深度小于等于3
    def toTree3(self, t):
        n = len(t) - 1
        for i in range(1, n - 1):
            for j in range(2 * i):
                if t[i][j] == '.':
                    t[i + 1].insert(j + 1, '.')
                    t[i + 1].insert(j + 1, '.')
        result = []
        result.append('   {}   '.format(t[0][0]))
        result.append('  / \\  ')
        result.append(' {}   {} '.format(t[1][0], t[1][1]))
        result.append('/ \\ / \\')
        result.append('{} {} {} {}'.format(*t[2]))
        for i in result[:2 * n - 1]:
            print(i)

    # 二叉树按层序转换为列表
    def treeArray(self, pRoot):
        if not pRoot:
            return []
        resultList = []
        curLayer = [pRoot]
        while curLayer:
            curList = []
            nextLayer = []
            for node in curLayer:
                if node == '.':
                    curList.append('.')
                else:
                    curList.append(node.val)
                    if node.left:
                        nextLayer.append(node.left)
                    else:
                        nextLayer.append('.')
                    if node.right:
                        nextLayer.append(node.right)
                    else:
                        nextLayer.append('.')
            resultList.append(curList)
            curLayer = nextLayer
        return resultList

    # 将上两个函数合并
    def printTree(self, tree):
        a = self.treeArray(tree)
        if len(a) < 5:
            self.toTree3(a)
        else:
            self.toTree4(a)

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

# print(a.printTree(a))

# print("preorder Traversal: ", a.preorderTraversal(a))
# print("inorder Traversal: ", a.inorderTraversal(a))
# print("postorder Traversal: ", a.postorderTraversal(a))
# print("layerorder Traversal: ", a.layerorderTraversal(a))
