let nums = [5, 3, 2, 6, 0, 1, 3, 2, 4];
console.log('nums:', nums);

// 时间：N^2  空间：1  最好：N  最坏：N^2  In-place  稳定
function bubbleSort(nums) {
  const n = nums.length;
  let change = false;
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]];
        change = true;
      }
    }
    if (change === false) return nums;
  }
  return nums;
}
// console.log(bubbleSort(nums));


// 时间：N^2  空间：1  最好：N^2  最坏：N^2  In-place  不稳定
function selectSort(nums) {
  const n = nums.length;
  for (let i = 0; i < n - 1; i++) {
    let minidx = i
    for (let j = i + 1; j < n; j++) {
      if (nums[minidx] > nums[j]) {
        minidx = j;
      }
    }
    [nums[minidx], nums[i]] = [nums[i], nums[minidx]]
  }
  return nums;
}
// console.log('sort:', selectSort(nums));

// 时间：N^2  空间：1  最好：N  最坏：N^2  In-place  稳定
function insertSort(nums) {
  const n = nums.length;
  for (let i = 1; i < n; i++) {
    let j = i - 1;
    let cur = nums[i];
    while (j >= 0 && cur < nums[j]) {
      nums[j + 1] = nums[j];
      j--;
    }
    nums[j + 1] = cur;
  }
  return nums;
}
// console.log('sort:', selectSort(nums));


// 时间：NlogN  空间：1  最好：N  最坏：N^2  In-place  不稳定
function shellSort(nums) {

}

// 时间：NlogN  空间：N  最好：NlogN  最坏：NlogN  Out-place  稳定
function mergeSort(nums) {
  const n = nums.length;
  if (n > 1) {
    let mid = Math.floor(n / 2);
    let left = mergeSort(nums.slice(0, mid));
    let right = mergeSort(nums.slice(mid, n));
    nums = merge(left, right);
  }
  return nums;
}

function merge(left, right) {
  let res = [];
  let i = 0, j = 0;
  while (i < left.length && j < right.length) {
    res.push(left[i] < right[j] ? left[i++] : right[j++]);
  }
  return res.concat(i < left.length ? left.slice(i) : right.slice(j));
}

// console.log('merge sort:', mergeSort(nums));

// 时间：NlogN  空间：logN  最好：NlogN  最坏：N^2  In-place  不稳定
function quickSort(nums) {
  if (nums.length <= 1) return nums;
  quick_sort(nums, 0, nums.length - 1);
  return nums;
}

function quick_sort(nums, left, right) {
  if (nums.length > 1) {
    let pos = partition(nums, left, right);
    if (pos - 1 > left) {
      quick_sort(nums, left, pos - 1);
    }
    if (pos < right) {
      quick_sort(nums, pos, right);
    }
  }
}

function partition(nums, left, right) {
  let i = left, j = right;
  let pivot = nums[Math.floor((left + right) / 2)];
  while (i < j) {
    while (nums[i] < pivot) i++;
    while (nums[j] > pivot) j--;
    if (i <= j) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
      i++;
      j--;
    }
  }
  return i;
}


console.log('quick sort:', quickSort(nums));

// 时间：NlogN  空间：1  最好：NlogN  最坏：NlogN  In-place  不稳定
function heapSort(nums) {

}


// 时间：N+k  空间：k  最好：N+k  最坏：N+k  Out-place  稳定
function countSort(nums) {

}

// 时间：N+k  空间：N+k  最好：N+k  最坏：N^2  Out-place  稳定
function bucketSort(nums) {

}

// 时间：N+k  空间：N+k  最好：N+k  最坏：N*k  Out-place  稳定
function radixSort(nums) {

}