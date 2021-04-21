

/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function (s) {
    // 思路：动态规划
    const n = s.length;
    if (n === 0) {
        return 0;
    }
    if (s[0] === '0') {
        return 0;
    }
    let dp = new Array(n + 1).fill(0);
    dp[0] = 1;
    dp[1] = 1;
    for (let i = 2; i <= n; i++) {
        if (s[i - 1] != '0') {
            dp[i] = dp[i - 1];
        }
        if (s[i - 2] != '0' && Number(s[i-2] + s[i-1]) <= 26) {
            dp[i] += dp[i - 2];
        }
    }
    return dp[n];
};

let s = "1123"
/* 
1 1 2 3
11 2 3
1 12 3
1 1 23
11 23
*/
console.log(numDecodings(s));