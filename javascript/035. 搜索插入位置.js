/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    const n = nums.length;
    if (target > nums[n-1]) {
        return n;
    }
    if (target < nums[0]) {
        return 0;
    }
    let left = 0, right = n-1;
    while(left < right) {
        let mid = Math.floor((left + right) / 2);
        let num = nums[mid];
        if (num === target) {
            return mid;
        } else if (num < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return left;
};

let nums = [1,3,5,6], target = 7;
console.log(searchInsert(nums, target));