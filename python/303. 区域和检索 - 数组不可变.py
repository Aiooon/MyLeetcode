"""
给定一个整数数组 nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，
包含 i、j 两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，
包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
 

示例：

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
 

提示：

0 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= i <= j < nums.length
最多调用 104 次 sumRange 方法

date: 2021年3月2日
"""
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        # todo 前缀和
        self.sums = [0]
        _sums = self.sums
        """
        以单下划线开头，表示这是一个保护成员，
        只有类对象和子类对象自己能访问到这些变量。
        以单下划线开头的变量和函数被默认当作是内部函数，
        使用from module improt *时不会被获取，但是使用import module可以获取
        """
        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        sums = self.sums
        return sums[j + 1] - sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# NumArray = NumArray([-2, 0, 3, -5, 2, -1])
# param_1 = NumArray.sumRange(0, 2)
# param_2 = NumArray.sumRange(2, 5)
# param_3 = NumArray.sumRange(0, 5)

# print(param_1, param_2, param_3)


class forTes:
    def __init__(self, num: int):
        # super().__init__()
        self.aa = [0]
        self.bb = 0
        a = self.aa
        _b = self.bb
        a.append(num)
        _b += num

    def change(self, b: int):
        arr = self.aa
        nn = self.bb
        print(arr, nn)
        arr.append(b)
        print(arr)
        print(self.aa)

tes = forTes(1)
tes.change(2)