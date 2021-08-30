/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number[]}
 */
var getLeastNumbers = function (arr, k) {
  let quickSort = (arr, left, right) => {
    if (left >= right) {
      return ;
    }
    let pivot = arr[left];
    let i = left, j = right;
    while(i < j) {
      while(i < j && arr[j] >= pivot) j--;
      while(i < j && arr[i] <= pivot) i++;
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    [arr[left], arr[i]] = [arr[i], arr[left]];
    quickSort(arr, left, i - 1);
    quickSort(arr, i + 1, right);
  }

  quickSort(arr, 0, arr.length - 1);
  // return arr.slice(0, k);
  return arr;
};

console.log(getLeastNumbers([0,1,2,1], 1));