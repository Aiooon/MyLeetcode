#  !/usr/bin/env  python
#  -*- coding:utf-8 -*-
#  堆排序

import random
import time

def heapSort(arr):
    if arr == None or len(arr) < 2:
        return
    for i in range(len(arr)):
        heapInsert(arr, i)
    size = len(arr)
    size -= 1
    swap(arr, 0, size)
    while size > 0:
        heapify(arr, 0, size)
        size -= 1
        swap(arr, 0, size)

def heapInsert(arr, index):
    while arr[index] > arr[(int)((index - 1) / 2)]:
        swap(arr, index, (int)((index - 1) / 2))
        index = (int)((index - 1) / 2)

def heapify(arr, index, size):
    left = index * 2 + 1
    while left < size:
        largest = left + 1 if (left + 1 < size and arr[left + 1] > arr[left]) else left
        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        swap(arr, largest, index)
        index = largest
        left = index * 2 + 1

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]



# 对数器
# for test
def comparator(array):
    array.sort()

# for test
def generateRandomArray(maxSize, maxValue):
    random_list = []
    for i in range(maxSize):
        random_list.append(random.randint(0, maxValue))
    return random_list

# for test
def isEqual(arr1, arr2):
    if arr1 != arr2:
        return False
    else:
        return True


def test():
    testTime = 10000
    maxSize = 100
    maxValue = 100
    succed = True
    time_start = time.time()
    for i in range(testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1
        heapSort(arr1)
        comparator(arr2)
        if isEqual(arr1, arr2) is False:
            succed = False
            break
    time_end = time.time()
    print('Test time cost : ', time_end - time_start, 's')
    print("Nice!" if succed else "Fuck!")
    arr = generateRandomArray(maxSize, maxValue)
    print(arr)
    heapSort(arr)
    print(arr)


test()