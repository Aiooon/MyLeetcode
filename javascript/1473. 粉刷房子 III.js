/* 
思路：动态规划

房子编号 0 ~ m - 1
颜色编号 0 ~ n - 1
街区编号 0 ~ target - 1

状态：dp[i][j][k] 表示"前 i 个房子组成 k 个街区，且第 i 个房子漆成第 j 个颜色"的最小花费。
初始：dp[i][j][k] = ∞
转移：遍历 m 个房子的 n 个不同颜色，设第 i-1 个房子的颜色为 j0 ：
    - 若 houses[i] != -1，表示第 i 个房子已经有颜色，设这个颜色 houses[i] = j
        - 在 houses[i] != j 时：
            dp[i][j][k] = ∞,   (houses[i] != -1 && houses[i] != j)          转移 1
        - 在 houses[i] == j 时：
            若 j == j0, 则 dp[i][j][k] = dp[i-1][j][k]                       转移 2
            若 j != j0, 则 dp[i][j][k] = min(dp[i-1][j][k-1]) (遍历 j)       转移 3
    - 若 houses[i] == -1, 表示第 i 个房子还没有颜色，设将它涂成颜色 j, 花费为 cost[i][j]
        设第 i-1 个房子的颜色为 j0 ：
        若 j == j0, 则 dp[i][j][k] = dp[i-1][j][k]                           转移 4
        若 j != j0, 则 dp[i][j][k] = min(dp[i-1][j][k-1]) (遍历 j)           转移 5

返回：min(dp[m][][target])
*/

/**
 * @param {number[]} houses
 * @param {number[][]} cost
 * @param {number} m
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var minCost = function (houses, cost, m, n, target) {
    // 将颜色调整为从0开始编号，-1表示没有颜色
    houses = houses.map(c => --c);
    // 所有元素初始化为最大值，因为要求的是最小值，所以设为最大值对结果没有影响
    const dp =  new Array(m).fill(0)
                            .map(() => new Array(n).fill(0)
                            .map(() => new Array(target).fill(Number.MAX_VALUE)));
    
    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j){
            if (houses[i] !== -1 && j !== houses[i]){   // 转移 1
                continue;
            }

            for (let k = 0; k < target; ++k) {
                for (let j0 = 0; j0 < n; ++j0) {
                    if (j === j0){
                        if (i === 0){
                            if (k === 0){
                                dp[i][j][k] = 0;
                            }
                        } else {
                            dp[i][j][k] = Math.min(dp[i][j][k], dp[i - 1][j][k]);   // 转移 2 4
                        }
                    } else if (i > 0 && k > 0) {
                        dp[i][j][k] = Math.min(dp[i][j][k], dp[i - 1][j0][k - 1]);  // 转移 3 5
                    }
                }

                if (dp[i][j][k] !== Number.MAX_VALUE && houses[i] === -1) {
                    dp[i][j][k] += cost[i][j];
                }
            }
        }
    }

    let ans = Number.MAX_VALUE;
    for (let j = 0; j < n; ++j){
        ans = Math.min(ans, dp[m - 1][j][target - 1]);
    }
    return ans === Number.MAX_VALUE ? -1: ans;
};


