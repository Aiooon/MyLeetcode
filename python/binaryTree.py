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

# llist = [1, 2, 3, 4, 5]
# A = TreeNode(1)
# A.createTreeWithList(None, llist, 0)
# print(A.function(A))