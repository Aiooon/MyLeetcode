class Solution:
    def searchRange_1(self, nums, target: int):
        for i in range(len(nums)):
            if nums[i] == target:
                left_index = i
                break
        else:
            return [-1, -1]

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_index = j
                break
        return [left_index, right_index]

    def searchRange_2(self, nums, target: int):
        if nums==[]:
            return [-1, -1]
        elif target < nums[0] or target > nums[-1]:
            return [-1, -1]
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                low = high = mid
                while low-1 >= 0 and nums[low-1] == target:
                    low -= 1
                while high+1 < len(nums) and nums[high+1] == target:
                    high += 1
                return [low, high]
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
        return [-1, -1]


nums = [5, 7, 7, 8, 8, 10]
s = Solution()
target = 8
print(s.searchRange_1(nums, target))
print(s.searchRange_2(nums, target))
