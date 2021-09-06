/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let l = 0, r = nums.length;
  while (l <= r) {
    if (nums[l] + nums[r] === target) {
      return [nums[l], nums[r]];
    } else if (nums[l] + nums[r] < target) {
      l++;
    } else {
      r--;
    }
  }
  return [];
};