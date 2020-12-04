"""
剑指 Offer 19. 正则表达式匹配
请实现一个函数用来匹配包含'. '和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。

注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/

date : 12-3-2020
"""


class Solution:
    """
    思路：
    当遇到 * 时：
        1. * 前的元素在 s 中出现 0 次：则 p 剪掉 * 和 * 前的元素，剩余的部分继续和 s 比较
        2. * 前的元素在 s 中出现 1 次或多次：如果 s 当前元素与 * 前的元素相同，则 s 剪掉当前元素，剩余部分继续与 p 比较
    当没有遇到 * 时：
        若当前两个元素相同，则 s 和 p 都剪掉当前元素，继续比较后面的部分；若不同则为 false
    """
    def isMatch_recur(self, s: str, p: str) -> bool:
        if p == "":
            return s == ""
        first_match = s != "" and (s[0] == p[0] or p[0] == ".")
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch_recur(s, p[2:]) or (first_match and self.isMatch_recur(s[1:], p))
        else:
            return first_match and self.isMatch_recur(s[1:], p[1:])

    def is_match(self, s: str, p: str, i, j) -> bool:
        return s[i] == p[j] or p[j] == '.'

    def isMatch_dp(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]

        #  初始化   dp[i][j] 代表字符串 s 的前 i 个字符和 p 的前 j 个字符能否匹配。
        dp[0][0] = True
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] or self.is_match(s, p, i - 1, j - 2) and dp[i - 1][j]
                else:
                    dp[i][j] = self.is_match(s, p, i - 1, j - 1) and dp[i - 1][j - 1]

        return dp[-1][-1]


s = "aaaa"
p = "a*a"

print(Solution().isMatch_dp(s, p))
print(Solution().isMatch_recur(s, p))

