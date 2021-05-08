
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
var rob = function (root) {
    if (root == null){
        return 0;
    }
    let money = root.val;
    if (root.left !== null){
        money += rob(root.left.left) + rob(root.left.right);
    }
    if (root.right !== null){
        money += rob(root.right.left) + rob(root.right.right);
    }
    return Math.max(money, rob(root.left) + rob(root.right));
};