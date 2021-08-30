
// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {number[][]}
 */
var pathSum = function(root, target) {
  let res = [], path = [];
  let dfs = (node, sum) => {
    if (!node) {
      return ;
    }
    path.push(node.val);
    sum -= node.val;
    if (sum === 0 && !node.left && !node.right) {
      res.push(path.slice());
    }
    dfs(node.left, sum);
    dfs(node.right, sum);
    path.pop();
  }
  dfs(root, target);
  return res;
};

/* 
    1
   / \
  2   3
 /    \
4      3
*/
var e = new TreeNode(3);
var d = new TreeNode(4);
var c = new TreeNode(3, null, e);
var b = new TreeNode(2, d);
var a = new TreeNode(1, b, c);


console.log(pathSum(a, 7));