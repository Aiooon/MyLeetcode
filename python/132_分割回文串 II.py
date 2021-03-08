"""
132. 分割回文串 II
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
返回符合要求的 最少分割次数 。

示例 1：
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

示例 2：
输入：s = "a"
输出：0

示例 3：
输入：s = "ab"
输出：1

提示：
1 <= s.length <= 2000
s 仅由小写英文字母组成

date: 2021年3月8日
"""

class Solution:
    def minCut(self, s: str) -> int:
        # self.isPalindrome = lambda s : s == s[::-1]
        # todo 两次动态规划
        """
        dp[i] 表示 s[0,i] 的最小分割数，用指针 j 切分成两个部分：
        s[0:j] 和 s[j+1:i]，那么 s[0,i] 的最小分割数就取决于这两个部分
        s[0:j] 的最小分割数是 dp[j] 已经计算过了，只需要找到 dp[i] 和 dp[j] 的递推关系
        如果 s[j+1:i] 是回文串，那么 dp[i] 就等于在 j 除再分割一次
        即 dp[i] = dp[j] + 1
        j 的范围是 [0, i), dp[i] 只要保存最小的 dp[j] + 1 即可

        Args:
            s (str): [description]

        Returns:
            int: [description]
        """
        N = len(s)
        isPalindrome = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):      # 第一次动规  记录s[j:i]是否是回文串
            for j in range(i + 1):
                if i == j:
                    isPalindrome[j][i] = 1
                elif i - j == 1 and s[i] == s[j]:
                    isPalindrome[j][i] = 1
                elif i - j > 1 and s[i] == s[j] and isPalindrome[j+1][i-1]:
                    isPalindrome[j][i] = 1
                else:
                    isPalindrome[j][i] = 0

        dp = [i for i in range(N)]
        for i in range(N):      # 第二次动规  记录s[0:i]的最小分割次数
            if isPalindrome[0][i]:
                dp[i] = 0
                continue
            for j in range(i):
                if isPalindrome[j+1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[N - 1]


s = "ababababa"
print(Solution().minCut(s))