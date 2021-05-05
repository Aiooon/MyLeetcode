/* 
740. 删除并获得点数
给你一个整数数组 nums ，你可以对它进行一些操作。
每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

示例 1：
输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。

示例 2：
输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104

date: 2021年5月5日
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var deleteAndEarn = function (nums) {
    /* 思路：动态规划
    用一个数组 cnt 统计每个数字出现的次数，数组的下标表示nums中的数字，例如：
    nums = [2,2,3,3,3,4]
    cnt  = [0,0,2,3,1]
    表示有 0个0，0个1，2个2，3个3，4个4
    然后对于 cnt 数组动态规划：
    dp[i] = max(dp[i-1], dp[i-2] + i * cnt[i])
    */
    let cnt = new Array(Math.max(...nums) + 1).fill(0);
    for (const n of nums){
        cnt[n]++;
    }
    let dp = new Array(cnt.length).fill(0);
    dp[1] = cnt[1];
    for (let i = 2; i < dp.length; ++i){
        dp[i] = Math.max(dp[i-1], dp[i-2] + i * cnt[i]);
    }
    return dp[dp.length - 1];
};

const nums = [2,2,3,3,3,4];
console.log(deleteAndEarn(nums));