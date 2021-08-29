/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function (coins, amount) {
  let dp = new Array(amount + 1).fill(amount + 1);
  dp[0] = 0;

  // for (let i = 0; i <= amount; i++) {
  //   for (coin of coins) {
  //     if (i < coin) {
  //       continue;
  //     }
  //     dp[i] = Math.min(dp[i], dp[i - coin] + 1);
  //   }
  // }
  
  // 更快的解法
  for (coin of coins) {
    for (let i = coin; i <= amount; i++) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }

  return dp[amount] === amount + 1 ? -1 : dp[amount];
};

const coins = [1,2,5];
console.log(coinChange(coins, 11));
