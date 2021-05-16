/**
 * @param {number[]} nums
 * @return {number}
 */
// 暴力法
var findMaximumXOR = function (nums) {
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            ans = Math.max(ans, nums[i] ^ nums[j]);
        }
    }
    return ans;
};

// todo 字典树
