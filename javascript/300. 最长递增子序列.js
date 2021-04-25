/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function (nums) {
    let n = nums.length;
    let dp = new Array(n).fill(1);
    let maxLen = 1;
    for (let i = 1; i < n; i++) {
        for (let j = i - 1; j >= 0; j--) {
            if (nums[j] < nums[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
                if (dp[i] > maxLen) {
                    maxLen = dp[i];
                }
            }
        }
    }
    return maxLen;
};

let nums = [0,1,0,3,2,3];
console.log(lengthOfLIS(nums));