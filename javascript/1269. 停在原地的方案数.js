/**
 * @param {number} steps
 * @param {number} arrLen
 * @return {number}
 */
var numWays = function (steps, arrLen) {
    /* 
    思路：动态规划
    状态：dp[i][j] i 步操作后指针停在 j 处的方案数
    初始：dp[0][0] = 1，当 1 <= j <= min(arrLen - 1, steps) 时，dp[0][j] = 0
    转移：每一步操作中，指针可以向左或向右移动 11 步，或者停在原地。因此，当 1 ≤ i ≤ steps 时，
        状态 dp[i][j] 可以从 dp[i−1][j−1]、dp[i−1][j] 和dp[i−1][j+1] 这三个状态转移得到。
        dp = dp[i−1][j−1] + dp[i−1][j] + dp[i−1][j+1]
     */
    const MOD = 10**9 + 7;
    const maxcol = Math.min(steps, arrLen - 1);
    let dp = new Array(steps + 1).fill(0).map(() => new Array(maxcol + 1).fill(0));
    dp[0][0] = 1;
    for (let i = 1; i <= steps; i++) {
        for (let j = 0; j <= maxcol; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j - 1 >= 0) {       // 当 j-1 >= 0 时，可以通过从 j-1 右移一步得到
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD;
            }
            if (j + 1 <= maxcol) {  // 当 j+1 <= maxcol 时，可以通过从 j+1 左移一步得到
                dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % MOD;
            }
        }
    }
    return dp[steps][0];
};