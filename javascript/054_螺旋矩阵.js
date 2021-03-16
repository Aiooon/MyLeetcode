/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
    if (!matrix) {
        return [];
    }
    let left = 0, right = matrix[0].length - 1;
    let top = 0, bot = matrix.length - 1;
    let res = new Array();

    while (true) {
        for (let i = left; i <= right; i++) {
            res.push(matrix[top][i]);
        }
        top++;
        if (top > bot) break;

        for (let i = top; i <= bot; i++) {
            res.push(matrix[i][right]);
        }
        right--;
        if (left > right) break;

        for (let i = right; i >= left; i--) {
            res.push(matrix[bot][i]);
        }
        bot--;
        if (top > bot) break;

        for (let i = bot; i >= top; i--) {
            res.push(matrix[i][left]);
        }
        left++;
        if (left > right) break;
    }

    return res;
};


let matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
console.log(spiralOrder(matrix));