"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

"""


def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    if n < 3:
        return 0
    result = nums[0] + nums[1] + nums[2]
    if n == 3:
        return result
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            min_ = nums[i] + nums[left] + nums[left+1]
            if min_ > target:
                if abs(min_-target) < abs(result-target):
                    result = min_
                break
            max_ = nums[i] + nums[right] + nums[right-1]
            if max_ < target:
                if abs(max_ - target) < abs(result - target):
                    result = max_
                break
            sum_ = nums[i] + nums[left] + nums[right]
            if sum_ == target:
                return sum_
            elif abs(sum_ - target) <= abs(result - target):
                result = sum_
            if sum_ > target:
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                right -= 1
            if sum_ < target:
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                left += 1
        while i < n-2 and nums[i] == nums[i+1]:
            i += 1
        i += 1
    return result


nums = [-1, 0, 1, 1, 55]
target = 3
print(threeSumClosest(nums, target))
