/**
 * @param {number[]} nums
 * @return {string}
 */
var minNumber = function(nums) {
  let quickSort = (nums, left, right) => {
    if (left >= right) {
      return ;
    }
    let i = left, j = right;
    let pivot = nums[i]

    while (i < j) {
      while (i < j && '' + pivot + nums[j] <= '' + nums[j] + pivot) j--;
      while (i < j && '' + nums[i] + pivot <= '' + pivot + nums[i]) i++;
      [nums[i], nums[j]] = [nums[j], nums[i]];
    }
    [nums[left], nums[i]] = [nums[i], nums[left]];

    quickSort(nums, left, i - 1);
    quickSort(nums, i + 1, right);
  }
  quickSort(nums, 0, nums.length - 1);
  return nums.join('');
};


let nums = [9, 2, 10];
console.log(minNumber(nums));
