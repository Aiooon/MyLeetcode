/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isStraight = function (nums) {
  nums = nums.sort((a, b) => a - b);
  let k = 0;
  for (let i = 0; i < 4; i++) {
    if (nums[i] === 0) {
      k++;
    } else if (nums[i] === nums[i + 1]) {
      return false;
    }
  }
  return nums[4] - nums[k] < 5;
};

console.log(isStraight([10,11,0,12,6]));