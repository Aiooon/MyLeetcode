/* 5711. 有界数组中指定下标处的最大值
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

示例 1：
输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。

示例 2：
输入：n = 6, index = 1,  maxSum = 10
输出：3

提示：
1 <= n <= maxSum <= 109
0 <= index < n 

date: 2021年3月21日
*/

/**
 * @param {number} n
 * @param {number} index
 * @param {number} maxSum
 * @return {number}
 */
var maxValue = function(n, index, maxSum) {
    let left = right = index;
    let res = 1, restSum = maxSum - n; 

    while(left > 0 || right < n -1) {
        let len = right - left + 1;
        if (restSum >= len){
            res++;
            restSum -= len;
            left = Math.max(0, left - 1);
            right = Math.min(n - 1, right + 1);
        } else break;
    }
    res += restSum / n;
    return parseInt(res);
};

let n = 963395373, index = 466661373,  maxSum = 964736618;
console.log(maxValue(n, index, maxSum));