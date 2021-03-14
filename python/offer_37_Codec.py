"""
剑指 Offer 37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

date : 1-26-2021
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        que = [root]
        res = []
        while que:
            node = que.pop(0)
            if node:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else :
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return
        vals, i = data[1 : -1].split(','), 1
        root = TreeNode(vals[0])
        que = [root]
        while que:
            node = que.pop(0)
            if vals[i] != 'null':
                node.left = TreeNode(vals[i])
                que.append(node.left)
            i += 1
            if vals[i] != 'null':
                node.right = TreeNode(vals[i])
                que.append(node.right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    a, b, c, d, e = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
    a.left, a.right = b, c
    c.left, c.right = d, e
    codec = Codec()
    data = codec.serialize(a)
    # print(data)
    # print(codec.deserialize(data))
