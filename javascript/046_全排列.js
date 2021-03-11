/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permute = function (nums) {
    var res = [];
    // var check = new Array(nums.length);
    // check.fill(0);
    backtrack([], nums, res);
    return res;
};

var backtrack = function (sol, nums, res) {
    if (sol.length == nums.length) {
        res.push(sol.slice());
        return
    }
    for (var i = 0; i < nums.length; i++) {
        if (sol.includes(nums[i])) {
            continue
        }
        sol.push(nums[i]);
        backtrack(sol, nums, res);
        sol.pop();
    }
}


var nums = [1, 2, 3];
console.log(permute(nums));
