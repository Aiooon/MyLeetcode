from typing import List
from operator import mul
from functools import reduce


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
        其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
        示例:
            输入: [1,2,3,4]
            输出: [24,12,8,6]
        提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
        说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
        :param nums:
        :return:
        """

        length = len(nums)

        # output = []
        # for i in range(length):
        #     if i == 0:
        #         output.append(reduce(mul, nums[1: length]))
        #     elif i == length - 1:
        #         output.append(reduce(mul, nums[0: length-1]))
        #     else:
        #         output.append(reduce(mul, nums[0: i]) * reduce(mul, nums[i+1: length]))
        # return output

        # L, R, ans = [0]*length, [0]*length, [0]*length
        # L[0] = 1
        # for i in range(1, length):
        #     L[i] = L[i - 1] * nums[i - 1]
        #
        # R[length - 1] = 1
        # for i in reversed(range(length-1)):
        #     R[i] = R[i + 1] * nums[i + 1]
        #
        # for i in range(length):
        #     ans[i] = L[i] * R[i]
        # return ans

        ans = [0]*length
        ans[0] = 1
        for i in range(1, length):
            ans[i] = ans[i - 1] * nums[i - 1]

        R = 1
        for i in reversed(range(length)):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans

s = Solution()
nums = [1,2,3,4,5]
print(s.productExceptSelf(nums))

# print(nums[0:2])
# print(nums[2:4])
# print(reduce(mul, nums[0:2]))

# print(reduce(mul, range(1, 5)))