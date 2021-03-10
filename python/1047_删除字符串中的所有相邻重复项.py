"""
1047. 删除字符串中的所有相邻重复项
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

提示：
1 <= S.length <= 20000
S 仅由小写英文字母组成。

date: 2021年3月9日
"""

class Solution:
    def removeDuplicates(self, S: str) -> str:
        """
        todo 栈
        s 中的字符依次入栈，若当前入栈元素与栈顶元素相同则舍弃掉，并将栈顶元素出栈

        Args:
            S (str): [description]

        Returns:
            str: [description]
        """
        if not S:
            return ""
        res = []
        for c in S:
            if not res:
                res.append(c)
            elif c == res[-1]:
                res.pop()
            else:
                res.append(c)
        return "".join(res)


s = 'abbaca'
print(Solution().removeDuplicates(s))