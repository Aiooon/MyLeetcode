/* 
剑指 Offer 07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
    3
   / \
  9  20
    /  \
   15   7

限制：
0 <= 节点个数 <= 5000

注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

date: 2021年6月26日
 */


// Definition for a binary tree node.
function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
    if (!preorder.length || !inorder.length) {
        return null;
    }
    let dic = new Map();
    // 建立字典，映射 preorder节点 -> 在中序遍历中的索引
    for (let i = 0; i < inorder.length; i++) {
        dic.set(inorder[i], i);
    }
    /* 
    root 表示当前根节点在前序遍历中的索引
    left 表示子树在中序遍历的左边界
    right 表示子树在中序遍历的右边界
     */
    var recur = function (root, left, right) {
        if (left > right) return null;  // 当左边界大于右边界时终止递归
        let node = new TreeNode(preorder[root]);  // 创建根节点
        let i = dic.get(preorder[root]);    // i 表示root在中序遍历中的索引，用来划分根节点、左子树、右子树
        node.left = recur(root + 1, left, i - 1);  // 开启左子树递归
        node.right = recur(i - left + root + 1, i + 1, right);  // 开启右子树递归
        return node;    // 返回根节点
    }
    return recur(0, 0, inorder.length - 1);
};


const preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7];
console.log(buildTree(preorder, inorder));

