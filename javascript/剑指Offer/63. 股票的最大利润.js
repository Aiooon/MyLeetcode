/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  // let dp = new Array(prices.length).fill(0);
  
  // for (let i = 1; i < prices.length; i++) {
  //   dp[i] = Math.max(dp[i - 1], prices[i] - Math.min(...prices.slice(0, i)));
  // }

  // return dp[prices.length - 1];
  let profit = 0;
  let cost = Number.MAX_VALUE;
  for (price of prices) {
    cost = Math.min(cost, price);
    profit = Math.max(profit, price - cost);
  }
  return profit;
};

// console.log(maxProfit([7,1,5,3,6,4]));
// console.log([7,1,5,3,6,4].slice(0, 2));

let a = new Array(3).fill(0);
console.log(a);
let b = a.slice(0)
a.length = 0;
console.log(a, b);
