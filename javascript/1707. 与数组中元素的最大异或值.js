/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
// todo 暴力法  超时
var maximizeXor = function (nums, queries) {
    const n = nums.length, m = queries.length;
    let ans = new Array(m).fill(-1);
    for (let i = 0; i < m; i++) {
        let x = queries[i][0], ma = queries[i][1];
        let res = 0;
        for (let j = 0; j < n; j++) {
            if (nums[j] <= ma) {
                res = Math.max(res, nums[j] ^ x);
            }
        }
        if (res !== 0) {
            ans[i] = res;
        }
    }
    return ans;
};