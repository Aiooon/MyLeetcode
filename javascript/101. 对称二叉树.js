
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
    if (root == null) return true;
    return isSymmetricChild(root.left, root.right);
};

var isSymmetricChild = function (left_child, right_child) {
    if (!left_child && !right_child) return true;
    if (!left_child || !right_child) return false;
    if (left_child.val != right_child.val) return false;
    return isSymmetricChild(left_child.left, right_child.right)
        && isSymmetricChild(left_child.right, right_child.left)
}