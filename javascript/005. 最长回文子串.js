/* 5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成 

date: 2021年3月22日
*/

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    /**
     * 状态：dp[i][j] 表示 s[i:j] 是否是回文串
     * 转移方程：dp[i][j] = s[i]==s[j] && dp[i+1, j-1]
     * base case: dp[i][i] = true (0 <= i <= s.length) 
     */
    const len = s.length;
    if (len < 2) {
        return s;
    }
    const dp = new Array(len).fill(0).map(() => new Array(len).fill(0));

    let start = 0;
    let max_len = 1;

    for (let i = 0; i < len; i++){
        dp[i][i] = 1;
    }

    for (let j = 1; j < len; j++){
        for (let i = 0; i < j; i++){
            if (s[i] == s[j]){
                if (j - i < 3){
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i+1][j-1]
                }
            } else {
                dp[i][j] = 0;
            }

            if ((dp[i][j] == 1) && ((j - i + 1) > max_len)) {
                max_len = j - i + 1;
                start = i;
            }
        }
    }
    return s.slice(start, start + max_len);
};

var huiwen = function (s) {
    return s.split('').reverse().join('') === s ? true : false;
}

s = 'abcbcb'
console.log(longestPalindrome(s))
