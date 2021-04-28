
//Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function (root, low, high) {
    // 思路：中序遍历，累加求和，提前返回
    let sum = 0;
    const dfs = (node) => {
        if (node == null) {
            return;
        }
        dfs(node.left);
        if (low <= node.val && node.val <= high){
            sum += node.val;
        }
        dfs(node.right);
    }
    dfs(root);
    return sum;
};


let a = new TreeNode(5);
let b = new TreeNode(2);
let c = new TreeNode(7);
let d = new TreeNode(8);
a.left = b;
a.right = c;
c.right = d;

console.log(rangeSumBST(a, 2, 5));