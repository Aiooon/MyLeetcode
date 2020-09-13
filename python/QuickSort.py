# Quick Sort
import random
import time
# import numpy as np
# x = np.empty([3,2], dtype = int)
# print (x)

def QuickSort(array):
    if array is None or array.__len__() < 2:
        return None
    quickSort(array, 0, array.__len__() - 1)

def quickSort(array, left, right):
    if left < right:
        # swap(array, left + (int)(random.random() * (right - left + 1)), right);
        p = partition(array, left, right)
        quickSort(array, 0, p[0] - 1)
        quickSort(array, p[1] + 1, right)


def partition(array, left, right):
    less = left - 1
    more = right
    cur = left
    while cur < more:
        if array[cur] < array[right]:
            less += 1
            swap(array, less, cur)
            cur += 1
        elif array[cur] > array[right]:
            more -= 1
            swap(array, more, cur)
        else:
            cur += 1
    swap(array, more, right)
    # print(array)
    return [less + 1, more]


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]



# for test
# 对数器
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
    testTime = 1000
    maxSize = 100
    maxValue = 100
    succed = True
    time_start = time.time()
    for i in range(testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = arr1
        QuickSort(arr1)
        comparator(arr2)
        if isEqual(arr1, arr2) is False:
            succed = False
            break
    time_end = time.time()
    print('Test time cost : ', time_end - time_start, 's')
    print("Nice!" if succed else "Fuck!")
    arr = generateRandomArray(maxSize, maxValue)
    print(arr)
    QuickSort(arr)
    print(arr)


test()

# if __name__ == '__main__':
#     array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#     quickSort(array, 0, array.__len__() - 1)
#     print(array)
