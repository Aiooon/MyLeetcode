/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var mirrorTree = function (root) {
  // dfs
  if (!root) {
    return null;
  }
  let tmp = root.left;
  root.left = mirrorTree(root.right);
  root.right = mirrorTree(tmp);
  return root;
};