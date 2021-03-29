/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
// var searchMatrix = function (matrix, target) {
//     const rows = matrix.length, cols = matrix[0].length;
//     let row = 0, col = cols - 1;
//     while (row < rows && col >= 0) {
//         if (matrix[row][col] == target) return true;
//         if (matrix[row][col] > target) col--;
//         if (matrix[row][col] < target) row++;
//     }
//     return false;
// };

// 二分法
var searchMatrix = function (matrix, target) {
    const rows = matrix.length, cols = matrix[0].length;
    let low = 0, high = rows * cols - 1;
    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        let x = matrix[Math.floor(mid / cols)][mid % cols];
        if (x < target) {
            low = mid + 1;
        } else if (x > target) {
            high = mid - 1;
        } else {
            return true;
        }
    }
    return false;
}

let matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 11
console.log(searchMatrix(matrix, target));