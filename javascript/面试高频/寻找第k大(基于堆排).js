/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function (nums, k) {
  if (nums.length === 1 && k === 1) {
    return nums[0];
  }
  return heapsortK(nums, k);
};

function heapsortK(nums, k) {
  for (let i = 0; i < nums.length; i++) {
    heapinsert(nums, i);
  }

  let heapsize = nums.length;

  swap(nums, 0, --heapsize);
  while (heapsize >= 0) {
    if (heapsize === nums.length - k) {
      return nums[heapsize];
    }
    heapify(nums, 0, heapsize);
    swap(nums, 0, --heapsize);
  }
}

function heapinsert(nums, index) {
  while (nums[index] > nums[Math.floor((index - 1) / 2)]) {
    swap(nums, index, Math.floor((index - 1) / 2));
    index = Math.floor((index - 1) / 2);
  }
}

function heapify(nums, index, heapsize) {
  let left = index * 2 + 1;
  while (left < heapsize) {
    let largest = left + 1 < heapsize && nums[left] < nums[left + 1] ? left + 1 : left;
    largest = nums[index] < nums[largest] ? largest : index;
    if (index === largest) {
      break;
    }
    swap(nums, index, largest);
    index = largest;
    left = index * 2 + 1;
  }
}

function swap(nums, i, j) {
  let tmp = nums[i];
  nums[i] = nums[j];
  nums[j] = tmp;
}

let nums = [2, 1], k = 2;
console.log(findKthLargest(nums, k));
