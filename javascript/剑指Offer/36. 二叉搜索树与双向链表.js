/**
 * // Definition for a Node.
 * function Node(val,left,right) {
 *    this.val = val;
 *    this.left = left;
 *    this.right = right;
 * };
 */
/**
 * @param {Node} root
 * @return {Node}
 */
var treeToDoublyList = function (root) {
  if (!root) {
    return null;
  }

  const dfs = (cur) => {
    if (!cur) {
      return null;
    }
    dfs(cur.left);
    if (!pre) {
      head = cur;
    } else {
      pre.right = cur;
      cur.left = pre;
    }
    pre = cur;
    dfs(cur.right);
  }
  let head = null, pre = null;
  dfs(root);
  head.left = pre;
  pre.right = head;
  return head;
};