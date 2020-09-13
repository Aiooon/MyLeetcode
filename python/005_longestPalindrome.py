class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 马拉车算法
        # 先在字符串中间加符号隔开，使得奇偶回文数的形式统一
        # 然后用kmp的思想去优化中心扩散
        if len(s) == 0: return ""
        s_new = '#' + '#'.join(s) + '#'
        # print(s_new)

        # 已遍历的最大右边界
        mx = 0
        # 对应的中心点
        mid = 0

        l = len(s_new)
        # 扩散半径数组，初始值1或者0都可以，只是代表刚开始的时候扩散半径是多少而已
        p = [1] * l

        for i in range(l):
            if i < mx:
                # 这个时候可以用已经计算过的值
                # 不能超过已遍历的右边界
                # i对应的镜像 = 2*mid - i
                # 由mx定义可知半径最长不会超过mx-i
                p[i] = min(mx - i, p[2 * mid - i])

            # 主要的优化已经在上面节省了时间，接下来就是正常的扩散
            while (i - p[i] >= 0 and i + p[i] < l and s_new[i - p[i]] == s_new[i + p[i]]):
                p[i] += 1

            # 记录一下mx和mid
            if i + p[i] > mx:
                mx = i + p[i]
                mid = i

        maxr = max(p)
        ans = p.index(maxr)
        # 因为跳出循环的时候多加了1，所以实际上的扩散半径应该减1
        maxr -= 1

        return s_new[ans - maxr:ans + maxr + 1].replace('#', "")


ss = Solution()
s = "aaaaaaaaaaaaasfaadgagasfgaaaaa"
print(ss.longestPalindrome(s))
