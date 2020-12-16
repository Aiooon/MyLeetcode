import random
from typing import List


def quickSort(nums: List[int]):
    if len(nums) < 1:
        return
    else:
        quick_sort(nums, 0, len(nums)-1)


def quick_sort(nums: List[int], left: int, right: int):
    if left < right:
        rdn = random.randint(left, right)   # random select num for partition
        nums[left], nums[rdn] = nums[rdn], nums[left]
        pivot_pos = partition(nums, left, right)
        quick_sort(nums, left, pivot_pos)
        quick_sort(nums, pivot_pos + 1, right)


def partition(nums: List[int], left: int, right: int):
    pivot, fin_pos = nums[left], left
    for i in range(left + 1, right + 1):
        if nums[i] <= pivot:
            fin_pos += 1
            nums[i], nums[fin_pos] = nums[fin_pos] , nums[i]
    nums[left], nums[fin_pos] = nums[fin_pos], nums[left]
    return fin_pos

# 在O(n)内查找第K大的数
def find_Kth_num(nums: List[int], k: int):
    l = len(nums)
    if l < 1 or l < k:
        return False
    left, right = 0, l-1
    while left < right:
        pivot_pos = partition(nums, left, right)
        if pivot_pos + 1 == k:
            return nums[pivot_pos]
        elif pivot_pos + 1 < k:
            left = pivot_pos + 1
        elif pivot_pos + 1 > k:
            right = pivot_pos - 1


if __name__ == '__main__':
    nums = [i for i in range(100)]
    ans = nums
    random.shuffle(nums)
    # print(nums)
    quickSort(nums)
    print(nums is ans)
    nums1 = [i for i in range(10)]
    random.shuffle(nums1)
    print(nums1)
    print(find_Kth_num(nums1, 6))


