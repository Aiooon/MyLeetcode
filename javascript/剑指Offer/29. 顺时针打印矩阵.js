/* 
剑指 Offer 29. 顺时针打印矩阵
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。


示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

date: 2021年8月16日
*/

/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
  if (!matrix.length) {
    return [];
  }
  let left = 0, right = matrix[0].length-1;
  let top = 0, bot = matrix.length-1;
  const res = [];
  while (true) {
    // left to right
    for (let i = left; i <= right; i++) {
      res.push(matrix[top][i]);
    }
    top++;
    if (top > bot) {
      break;
    }
    // top to bot
    for (let i = top; i <= bot; i++) {
      res.push(matrix[i][right]);
    }
    right--;
    if (left > right) {
      break;
    }
    // right to left
    for (let i = right; i >= left; i--) {
      res.push(matrix[bot][i]);
    }
    bot--;
    if (top > bot) {
      break;
    }
    // bot to top
    for (let i = bot; i >= top; i--) {
      res.push(matrix[i][left]);
    }
    left++;
    if (left > right) {
      break;
    }
  }
  return res;
};

let matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
console.log(spiralOrder([[]]));
