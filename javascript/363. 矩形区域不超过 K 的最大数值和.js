/* 
思路：
固定左右边界，计算每行的和，找到上下边界

date：2021年4月22日
*/
/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var maxSumSubmatrix = function (matrix, k) {
    let rows = matrix.length, cols = matrix[0].length;
    let max = -Number.MAX_SAFE_INTEGER;
    for (let left = 0; left < cols; left++){    // 枚举左边界
        let rowSum = new Array(rows).fill(0);   // 初始化每行的和
        for (let right = left; right < cols; right++) {     // 枚举右边界
            for (let i = 0; i < rows; i++) {
                rowSum[i] += matrix[i][right];
            }
            max = Math.max(max, dpmax(rowSum, k));
            if (max === k) return k;
        }
    }
    return max;
};

// 在数组 rowSum 中，求不超过 k 的最大连续和
var dpmax = function (arr, k) {
    let max = -Number.MAX_SAFE_INTEGER;
    for (let l = 0; l < arr.length; l++) {
        let sum = 0;
        for (let r = l; r < arr.length; r++) {
            sum += arr[r];
            if (sum > max && sum <= k) max = sum;
            if (max == k) return k;
        }
    }
    return max;
}

let matrix = [[1,0,1],[0,-2,3]], k = 2;
console.log(maxSumSubmatrix(matrix, k));