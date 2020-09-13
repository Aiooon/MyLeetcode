def twoSum_1(nums, target):
    length = len(nums)
    j = -1
    for i in range(1, length):
        temp = nums[:i]
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])
            break
    if j >= 0:
        return [j, i]

def twoSum_2(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if (target - num) in hashmap:
            return [hashmap.get(target - num), i]
        hashmap[num] = i

def twoSum_3(nums, target):
    for i in range(len(nums)):
        if (target - nums[i]) in nums[:i]:
            return [nums.index(target-nums[i]), i]


nums = [2, 7, 11, 15]
print(list(enumerate(nums)))
target = 9
# print(twoSum_1(nums, target))
print(twoSum_2(nums, target))
print(twoSum_3(nums, target))