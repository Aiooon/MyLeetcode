/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
  if (nums.length === 0 || nums.length < k) {
    return [];
  }
  let j = k - 1;
  let window = nums.slice(0, k);
  let res = [Math.max(...window)];
  while (j < nums.length - 1) {
    j++;
    window.push(nums[j]);
    window.shift();
    res.push(Math.max(...window));
  }
  return res;
};


let s = "800 2 0"
console.log(s.split(' '));