/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(matrix) {
    const m = matrix.length, n = matrix[0].length;
    let col0 = false, row0 = false;     // col0, row0 分别记录第一行和第一列是否需要置0
    
    // 遍历第一行和第一列，标记是否需要置 0
    for (let i = 0; i < n; i++) {
        if (matrix[0][i] === 0) {
            row0 = true;
        }
    }
    for (let j = 0; j < m; j++) {
        if (matrix[j][0] === 0) {
            col0 = true;
        }
    }

    // 遍历非首行首列，将是否需要置 0 记录在首行首列中
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++) {
            if (matrix[i][j] === 0) {
                matrix[0][j] = matrix[i][0] = 0;
            }
        }
    }

    // 遍历非首行首列，根据首行首列的标记置 0
    for (let i = 1; i < m; i++) {
        for (let j = 1; j < n; j++){
            if (matrix[i][0] === 0 || matrix[0][j] === 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // 根据 row0 和 col0 给首行首列置 0
    if (col0) {
        for (let i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
    if (row0) {
        for (let j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }
};


const matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]];
setZeroes(matrix);
console.log(matrix);