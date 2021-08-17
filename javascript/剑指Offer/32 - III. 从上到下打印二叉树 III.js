/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
  // 之字形打印，奇数层从左到右，偶数层从右向左
  // 方法一：列表倒转
  // 方法二：双端队列，奇数层从队尾入队，偶数层从队头入队
  if (!root) {
    return [];
  }
  let queue = [root], res = [];
  let flag = false;
  while (queue.length !== 0) {
    let len = queue.length;
    let level = []
    for (let i = 0; i < len; i++) {
      let node = queue.shift();
      level.push(node.val);
      if (node.left !== null) {
        queue.push(node.left);
      }
      if (node.right !== null) {
        queue.push(node.right);
      }
    }
    res.push(flag? level.reverse() : level);
    flag = !flag
  }

  return res;
};

