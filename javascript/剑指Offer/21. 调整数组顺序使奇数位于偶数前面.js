/*
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：

0 <= nums.length <= 50000
1 <= nums[i] <= 10000

date: 2021年8月16日
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var exchange = function (nums) {
  let left = 0, right = nums.length - 1;  // left 从左往右找偶数，right 从右往左找奇数
  while (left < right) {
    while (left < right && nums[left] % 2 === 1) {
      left++;
    }
    while (left < right && nums[right] % 2 === 0) {
      right--;
    }
    let t = nums[left];
    nums[left] = nums[right];
    nums[right] = t;
  }
  return nums;
};

let nums = [1, 2, 3, 4, 5, 6, 7];
console.log(exchange(nums));