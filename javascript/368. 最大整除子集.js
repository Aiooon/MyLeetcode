/* 
368. 最大整除子集
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中 最大 的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

示例 1：
输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。

示例 2：
输入：nums = [1,2,4,8]
输出：[1,2,4,8]

提示：
1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 10^9
nums 中的所有整数 互不相同

date: 2021年4月23日
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var largestDivisibleSubset = function (nums) {
    /* 思路：动态规划
    首先按升序排序数组 nums，然后枚举每一项，dp[i] 记录包含 nums[i] 时的最大整除子集的大小，
    然后根据结果倒推得到最终的子集
    base：dp[i] = 1，因为必须包含 nums[i]
    状态 dp[i]：包含 nums[i] 的最大整除子集的大小
    转移：枚举 j = 0 ~ i-1 的所有 nums[j]，如果 nums[j] 能整除 nums[i]，则 dp[i] = Math.max(dp[i], dp[j] + 1)
    */

    nums.sort((a, b) => a - b);
    const n = nums.length;
    let res = [];
    let dp = new Array(n).fill(1);
    let maxSize = 1, maxVal = nums[0];
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[i] % nums[j] === 0) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
        if (dp[i] > maxSize) {
            maxSize = dp[i];
            maxVal = nums[i];
        }
    }

    if (maxSize === 1) {
        res.push(nums[0]);
        return res;
    }
    for (let i = n - 1; i >= 0 && maxSize > 0; i--) {
        if (dp[i] === maxSize && maxVal % nums[i] === 0) {
            res.unshift(nums[i]);
            maxSize--;
            maxVal = nums[i];
        }
    }
    return res;
};

let nums = [2, 4, 7, 8, 9, 12, 16, 18];
console.log(largestDivisibleSubset(nums));