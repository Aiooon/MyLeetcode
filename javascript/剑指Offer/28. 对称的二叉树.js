/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  if (!root) {
    return true;
  }

  var recur = function (left, right) {
    if (!left && !right) {
      return true;
    }
    if (!left || !right || left.val !== right.val) {
      return false;
    }
    return recur(left.left, right.right) && recur(left.right, right.left);
  }

  return recur(root.left, root.right)
};