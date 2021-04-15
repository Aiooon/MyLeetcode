/* 
783. 二叉搜索树节点最小距离
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同

示例 1：
输入：root = [4,2,6,1,3]
输出：1

示例 2：
输入：root = [1,0,48,null,null,12,49]
输出：1

提示：

树中节点数目在范围 [2, 100] 内
0 <= Node.val <= 10^5

date: 2021年4月13日
*/


// Definition for a binary tree node.

function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDiffInBST = function (root) {
    // 思路：递归
    let res = Number.MAX_SAFE_INTEGER, pre = -1;
    var dfs = function (root) {
        if (root === null) {
            return
        }
        dfs(root.left);
        if (pre == -1) {
            pre = root.val
        } else {
            res = Math.min(res, root.val - pre);
            pre = root.val;
        }
        dfs(root.right);
    }
    dfs(root);
    return res;
};

let a = new TreeNode(4), b = new TreeNode(2), c = new TreeNode(6), d = new TreeNode(1), e = new TreeNode(3);
a.left = b;
a.right = c;
b.left = d;
b.right = e;

console.log(minDiffInBST(a));