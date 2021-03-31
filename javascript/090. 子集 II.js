/*
思路： 
对于数组 [1,2,3] 
初始的子集为 [[]]
加入 1：[[],[1]]，即在 [] 中加入了 1
加入 2: [[],[1],[2],[1,2]]，即在 [],[1]，中加入了 2
加入 3: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] 即在 [],[1],[2],[1,2] 中加入了 3
处理重复数字：排序后用 visited 数组记录数字是否访问过，
若当前数字与前一个相同，且前一个没有访问过，说明同一层上有两个重复数字，则将当前数字不可以选择。
*/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function (nums) {
    let res = [];
    const n = nums.length;
    if (n == 0) return res;

    nums.sort((a, b) => a - b);
    let visited = new Array(n).fill(false);
    let path = [];

    var backtrack = function (nums, start, visited) {
        res.push(path.slice());
        for (let i = start; i < n; i++) {
            if (i > 0 && nums[i] == nums[i - 1] && visited[i - 1] == false) {
                continue;
            }
            path.push(nums[i]);
            visited[i] = true;
            backtrack(nums, i + 1, visited);
            visited[i] = false;
            path.pop();
        }
    }
    backtrack(nums, 0, visited, path);
    return res;
};



nums = [1, 2, 2];
console.log(subsetsWithDup(nums));
