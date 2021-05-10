/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSumMinProduct = function (nums) {
    // dp[i][j] 记录数组 nums 在 [i, j] 范围内子数组的和
    const n = nums.length;
    let dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
    for (let i = 0; i < n; ++i) {
        dp[i][i] = nums[i];
    }
    for (let i = 0; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            dp[i][j] = dp[i][j-1] + nums[j];
        }
    }
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        for (let j = i; j < n; ++j) {
            let mi = Math.min(...nums.slice(i,j+1));
            let cur = mi * dp[i][j];
            ans = Math.max(ans, cur);
        }
    }
    return ans % (10**9 + 7);
};


let nums = [3,1,5,6,4,2];
console.log(maxSumMinProduct(nums));
