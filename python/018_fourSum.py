"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


def fourSum(nums, target):
    n = len(nums)
    if n < 4:
        return []
    nums.sort()
    ans = []
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 如果最小的和都大于target  退出
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        # 如果最大的和都小于target  则i+1
        if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
            continue
        j = n-1
        while j > i+2:
            left, right = i+1, j-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right] + nums[j]
                if sum == target:
                    ans.append([nums[i], nums[left], nums[right], nums[j]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
            while j > i+2 and nums[j] == nums[j-1]:
                j -= 1
            j -= 1
    return ans


nums = [1, -2, -5, -4, -3, 3, 3, 5]
target = -11
print(fourSum(nums, target))
