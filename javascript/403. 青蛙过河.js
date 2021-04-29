/* 
403. 青蛙过河
一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。

开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。


示例 1：
输入：stones = [0,1,3,5,6,8,12,17]
输出：true
解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。

示例 2：
输入：stones = [0,1,2,3,4,8,9,11]
输出：false
解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。

提示：
2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0

date: 2021年4月29日
*/

/**
 * @param {number[]} stones
 * @return {boolean}
 */
var canCross = function (stones) {
    /* 思路：二维动态规划
    状态：dp[i][k] 表示 能否到达第 i 个石子，且上一次跳跃的距离为 k
    初始：dp[0][0] 表示第一个石子能到达，且上一次跳跃距离为 0
    转移：dp[i][k] = dp[j][k-1] || dp[j][k] || dp[j][k+1], 其中 j 表示上一次所在的石子，k = stones[i] = stones[j]
    
    对于第 i 个石子，枚举所有的 j (j < i)，那么当前的 k = stones[i] = stones[j]
    如果在第 j 个石子上，则上一次的跳跃距离可以是 k-1, k 或 k+1, 即 dp[j][k-1], dp[j][k], dp[j][k+1] 至少有一个为真即可
    */

    const n = stones.length;
    let dp = new Array(n).fill(0).map(() => new Array(n).fill(0));
    dp[0][0] = true;
    for (let i = 1; i < n; i++){
        if (stones[i] - stones[i-1] > i){   // 上一次的跳跃距离最多为 i-1，因此这次最多跳跃 i
            return false;
        }
    }
    for (let i = 1; i < n; i++) {
        for (let j = i-1; j >= 0; j--) {
            let k = stones[i] - stones[j];
            if (k > j + 1) {    // 在第 j 个石子上虽多跳跃 j+1 格
                break;
            }
            dp[i][k] = dp[j][k-1] || dp[j][k] || dp[j][k+1];
            if (i === n-1 && dp[i][k]){
                return true;
            }
        }
    }
    return false;
};

let stones = [0,1,3,5,6,8,12,17];
console.log(canCross(stones));