/* 
132. 分割回文串 II
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
返回符合要求的 最少分割次数 。

示例 1：
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

示例 2：
输入：s = "a"
输出：

示例 3：
输入：s = "ab"
输出：1

提示：
1 <= s.length <= 2000
s 仅由小写英文字母组成

date: 2021年3月29日
*/

/**
 * @param {string} s
 * @return {number}
 */
var minCut = function(s) {
    const n = s.length;
    let huiwen = new Array(n).fill(false).map(() => new Array(n).fill(false));
    // huiwen 数组记录回文信息  huiwen[i][j]=1 表示 s[i:j+1]是回文
    for (let j = 0; j < n; j++) {
        for (let i = 0; i < j+1; i++) {
            if (i == j) {
                huiwen[i][j] = true;
            } else if ((j - i == 1) && s[i] == s[j]) {
                huiwen[i][j] = true;
            } else if (j-i > 1 && s[i] == s[j] && huiwen[i+1][j-1]) {
                huiwen[i][j] = true;
            }
        }
    }
    /* 
    dp[i] 表示 i 处的最少分割次数
    对于分割次数的分析：
    在位置 j,
    若 s[0;j+1] 是回文串，则 dp[j] = 0
    若 s[0;j+1] 不是回文：
        s[j] 单独切割，则 dp[j] = dp[j-1]+1
        s[i:j] 形成回文，则 dp[j] = dp[i-1] + 1
    */
    let dp = new Array(n);
    // for (let i = 0; i < n; i++) dp[i] = i;
    for (let j = 0; j < n; j++){
        if (huiwen[0][j]){
            dp[j] = 0;
            continue;
        }
        dp[j] = dp[j-1] + 1
        for (let i = 0; i < j; i++){
            if (huiwen[i][j]){
                dp[j] = Math.min(dp[j], dp[i-1] + 1);
            }
        }
    }
    return dp[n-1];
}; 

s = 'aabbc';
console.log(minCut(s));