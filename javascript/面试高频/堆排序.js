function heapSort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  for (let i = 0; i < arr.length; i++) {
    heapInsert(arr, i);
  }

  let heapsize = arr.length;
  swap(arr, 0, --heapsize);
  while (heapsize > 0) {
    heapify(arr, 0, heapsize);
    swap(arr, 0, --heapsize);
  }

  return arr;
}

// 向上比较，大于父节点就和父节点交换
function heapInsert(arr, index) {
  while (arr[index] > arr[Math.floor((index - 1) / 2)]) {
    swap(arr, index, Math.floor((index - 1) / 2));
    index = Math.floor((index - 1) / 2);
  }
}

// 向下比较，某个数在index位置，能否往下移动
function heapify(arr, index, heapsize) {
  let left = 2 * index + 1;
  while (left < heapsize) {
    let largest = left + 1 < heapsize && arr[left + 1] > arr[left] ? left + 1 : left;
    largest = arr[index] > arr[largest] ? index : largest;
    if (index === largest) {
      break;
    }
    swap(arr, index, largest);
    index = largest;
    left = index * 2 + 1;
  }
}

function swap(arr, i, j) {
  let tmp = arr[i];
  arr[i] = arr[j];
  arr[j] = tmp;
}

const arr = [1, 7, 2, 3, 6, 3, 8, 4 ,5, 0];
console.log(heapSort(arr));