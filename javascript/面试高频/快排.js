function quickSort(arr) {
  if (arr.length <= 1) {
    return arr;
  }
  quick_sort(arr, 0, arr.length - 1);
  return arr;
}


function quick_sort(arr, left, right) {
  if (left < right) {
    let pos = partition(arr, left, right);
    if (pos - 1 > left) {
      quick_sort(arr, left, pos - 1);
    }
    if (pos + 1 < right) {
      quick_sort(arr, pos + 1, right);
    }
  }
}

function partition(arr, left, right) {
  let pivot = arr[left];
  let mark = left;
  for (let i = mark + 1; i <= right; i++) {
    if (arr[i] < pivot) {   // 在循环中，mark表示小于 pivot 的部分的右边界
      mark++;
      [arr[mark], arr[i]] = [arr[i], arr[mark]];
    }
  }
  arr[left] = arr[mark];
  arr[mark] = pivot;
  return mark;
}

// function partition(arr, left, right) {
//   let i = left, j = right;
//   let pivot = arr[left];
//   while (i < j) {
//     while(arr[j] > pivot && i < j) j--;
//     // [arr[i], arr[j]] = [arr[j], arr[i]];
//     arr[i] = arr[j];
//     while(arr[i] < pivot && i < j) i++;
//     // [arr[i], arr[j]] = [arr[j], arr[i]];
//     arr[j] = arr[i];
//   }
//   arr[i] = pivot;
//   return i;
// }

let arr = [3, 1, 5, 2, 2];
console.log(partition(arr, 0, arr.length - 1));    
// console.log(quickSort(arr));