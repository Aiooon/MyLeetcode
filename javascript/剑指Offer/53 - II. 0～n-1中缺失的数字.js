/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function (nums) {
  let i = 0, j = nums.length - 1;
  while (i <= j) {
    let mid = Math.floor((i + j) / 2);
    if (nums[mid] === mid) {
      i = mid + 1;
    } else {
      j = mid - 1;
    }
  }
  return i;
};