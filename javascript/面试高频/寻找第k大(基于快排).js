// https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
  return quickSelect(nums, 0, nums.length - 1, nums.length - k);
};


function quickSelect(nums, left, right, index) {
  let pos = partition(nums, left, right);
  if (pos === index) {
    return nums[pos];
  }
  return pos < index ? quickSelect(nums, pos + 1, right, index) : quickSelect(nums, left, pos - 1, index);
}

function partition(nums, left, right) {
  let random = Math.floor(Math.random()*(right - left + 1) + left);
  swap(nums, left, random);
  const pivot = nums[left];
  let mark = left;
  for (let i = mark + 1; i <= right; i++) {
    if (nums[i] < pivot) {
      mark++;
      swap(nums, i, mark);
    }
  }
  nums[left] = nums[mark];
  nums[mark] = pivot;
  return mark;
}

function swap(arr, i, j) {
  let tmp = arr[i];
  arr[i] = arr[j];
  arr[j] = tmp;
}

let nums = [3,2,3,1,2,4,5,5,6], k = 4;
console.log(findKthLargest(nums, k));
