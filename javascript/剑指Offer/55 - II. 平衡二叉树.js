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
var isBalanced = function (root) {
  const recur = (root) => {
    if (!root) return 0;
    let left = recur(root.left);
    if (left === -1) return -1;
    let right = recur(root.right);
    if (right === -1) return -1;
    return Math.abs(left - right) <= 1 ? Math.max(left, right) + 1 : -1;
  }

  return recur(root) !== -1;
};