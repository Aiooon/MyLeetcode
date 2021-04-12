/* 
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

1  2  3    7  4  1
4  5  6 -> 8  5  2
7  8  9    9  6  3

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

示例 2：
输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

示例 3：
输入：matrix = [[1]]
输出：[[1]]

示例 4：
输入：matrix = [[1,2],[3,4]]
输出：[[3,1],[4,2]]

提示：

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

   1             3                  9                 7
0     0  ->   0     2    ->    2        2   ->    2      0
   2             6                  8                 4
0     1  ->   1     2    ->    2        1   ->    1      0
row col     col n-row-1     n-row-1  n-col-1   n-col-1  row
原 新
00 02       新的行坐标 = 原列坐标
01 12       新的列坐标 = matrix.length - 原行坐标 - 1
02 22

date: 2021年4月7日
*/

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function (matrix) {
    // 思路：计算每个数旋转后的坐标
    let n = matrix.length;
    for (let row = 0; row < Math.floor(n / 2); row++) {
        for (let col = 0; col < Math.floor((n + 1) / 2); col++) {
            let tmp = matrix[n - col - 1][row];
            matrix[n - col - 1][row] = matrix[n - row - 1][n - col - 1];
            matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1];
            matrix[col][n - row - 1] = matrix[row][col];
            matrix[row][col] = tmp;
        }
    }
};

// matrix = [[1,2,3],[4,5,6],[7,8,9]];
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]];
rotate(matrix);
console.log(matrix);