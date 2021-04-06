# 通过行列的值计算出前面有多少个数，然后对 9 取模

class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        left, right = 0, num - 1   # 列数的遍历范围  左 <-> 右
        top, bot = 0, num - 1           # 行数的遍历范围  上 <-> 下
        num = 1
        while True:
            for i in range(left, right + 1):    # 从左至右
                if top == xPos and i == yPos: return num
                num += 1
                if num == 10: num = 1
            top += 1
            
            for i in range(top, bot + 1):   # 从上至下
                if i == xPos and right == yPos: return num
                num += 1
                if num == 10: num = 1
            right -= 1
            
            for i in range(right, left - 1, -1):     # 从右至左
                if bot == xPos and i == yPos: return num
                num += 1
                if num == 10: num = 1
            bot -= 1

            for i in range(bot, top - 1, -1):       # 从下至上
                if i == xPos and left == yPos: return num
                num += 1
                if num == 10: num = 1
            left += 1


print(Solution().orchestraLayout(5,1,2))