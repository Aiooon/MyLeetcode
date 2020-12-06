"""
排序算法

"""
import random
from typing import List


class Sort:

    # 冒泡排序
    def bubble_sort(self, nums: List[int]):
        length = len(nums)
        if length <= 1:
            return

        for i in range(length):
            made_swap = False
            for j in range(length - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    made_swap = True
            if not made_swap:
                break

    # 插入排序
    def insertion_sort(self, nums: List[int]):
        length = len(nums)
        if length <= 1:
            return

        for i in range(1, length):
            value = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > value:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = value

    # 选择排序
    def selection_sort(self, nums: List[int]):
        length = len(nums)
        if length <= 1:
            return

        for i in range(length):
            min_index = i
            min_val = nums[i]
            for j in range(i, length):
                if nums[j] < min_val:
                    min_val = nums[j]
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]


if __name__ == '__main__':
    nums = [i for i in range(10)]
    Sort = Sort()

    random.shuffle(nums)
    print(nums)
    Sort.bubble_sort(nums)
    print(nums, '\n')

    random.shuffle(nums)
    print(nums)
    Sort.insertion_sort(nums)
    print(nums, '\n')

    random.shuffle(nums)
    print(nums)
    Sort.selection_sort(nums)
    print(nums, '\n')
