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

    # 归并排序
    def merge_sort(self, nums: List[int]):
        if len(nums) <= 1:
            return
        self._merge_sort(nums, 0, len(nums) - 1)

    def _merge_sort(self, nums: List[int], left: int, right: int):
        if left < right:
            mid = left + (right - left) // 2
            self._merge_sort(nums, left, mid)
            self._merge_sort(nums, mid + 1, right)
            self._merge(nums, left, mid, right)

    def _merge(self, nums: List[int], left: int, mid: int, right: int):
        tmp = []
        left_point, right_point = left, mid + 1
        while left_point <= mid and right_point <= right:
            if nums[left_point] <= nums[right_point]:
                tmp.append(nums[left_point])
                left_point += 1
            else:
                tmp.append(nums[right_point])
                right_point += 1
        start = left_point if left_point <= mid else right_point
        end = mid if left_point <= mid else right
        tmp.extend(nums[start:end + 1])
        nums[left:right + 1] = tmp

    def quick_sort(self, nums: List[int]):
        if len(nums) <= 1:
            return
        self._quick_sort(nums, 0, len(nums) - 1)

    def _quick_sort(self, nums: List[int], left: int, right: int):
        if left < right:
            # 随机选择一个数划分，将这个数换到第一个位置
            rdm = random.randint(left, right)
            nums[left], nums[rdm] = nums[rdm], nums[left]
            pivot_pos = self.partition(nums, left, right)
            self._quick_sort(nums, left, pivot_pos)
            self._quick_sort(nums, pivot_pos + 1, right)

    def partition(self, nums: List[int], left: int, right: int):
        # 将第一个数作为pivot， fin_pos记录pivot在nums中最终的位置
        pivot, fin_pos = nums[left], left
        for i in range(left + 1, right + 1):
            if nums[i] <= pivot:
                # 交换一次位置说明pivot左边的数的个数+1
                fin_pos += 1
                nums[i], nums[fin_pos] = nums[fin_pos], nums[i]
        # 循环结束后fin_pos就是pivot最终的位置，将
        nums[left], nums[fin_pos] = nums[fin_pos], nums[left]
        return fin_pos


if __name__ == '__main__':
    nums = [i for i in range(100)]
    ans = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    Sort = Sort()

    random.shuffle(nums)
    print("bubble_sort:")
    Sort.bubble_sort(nums)
    print("True"if nums == ans else "False")

    random.shuffle(nums)
    print("insertion_sort:")
    Sort.insertion_sort(nums)
    print("True"if nums == ans else "False")

    random.shuffle(nums)
    print("selection_sort:")
    Sort.selection_sort(nums)
    print("True"if nums == ans else "False")

    random.shuffle(nums)
    print("merge_sort:")
    Sort.merge_sort(nums)
    print("True"if nums == ans else "False")

    random.shuffle(nums)
    print("quick_sort:")
    Sort.quick_sort(nums)
    print("True"if nums == ans else "False")
