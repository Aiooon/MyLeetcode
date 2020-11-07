"""
面试题03. 题目2： 不修改数组找出重复的数字

在一个长度为 n + 1 的数组中所有的数字都在 1 ~ n 的范围内，所以数组中至少存在一个重复数字。
请找出数组中的任意一个重复数字，但不能修改输入的数组。
例如，如果输入长度为 8 的数组 [2, 3, 5, 4, 3, 2, 6, 7], 那么对应的输出是重复的数字 2 或 3

date ： 9-17-2020
"""


def findDuplication(nums, length):
    box = set()
    repeat = None
    for i in range(length):
        if not box.add(nums[i]):
            repeat = nums[i]
            break
    return repeat


def count(nums, length, start, end):
    """

    :param nums:
    :param length:
    :param start:
    :param mid:
    :return:
    """
    if nums is None:
        return 0

    count = 0
    for i in range(length):
        if start <= nums[i] <= end:
            count += 1
    return count


def getDuplication(nums, length):
    """

    :param nums:
    :param length:
    :return:
    """
    if nums is None:
        return 0

    start = 1
    end = length - 1
    while start < end:
        mid = int((start + end) / 2)
        countt = count(nums, length, start, mid)
        if end == start:
            if countt > 1:
                return start
            else:
                break
        if countt > mid - start + 1:
            end = mid
        else:
            start = mid + 1
    return -1


nums = [2, 3, 5, 4, 3, 2, 2, 6, 7]
length = 9
print(getDuplication(nums, length))

print(findDuplication(nums, length))
