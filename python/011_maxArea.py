"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


def maxArea(height):
        i, j = 0, len(height)-1
        maxarea = 0
        while i < j:
            if height[i] < height[j]:
                maxarea = max(maxarea, height[i] * (j - i))
                i += 1
            else:
                maxarea = max(maxarea, height[j] * (j - i))
                j -= 1
        return maxarea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
