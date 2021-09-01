/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
  const dp = new Array(n).fill(1);
  let a = 0, b = 0, c = 0;
  for (let i = 1; i < n; i++) {
    let u1 = dp[a] * 2, u2 = dp[b] * 3, u3 = dp[c] * 5;
    dp[i] = Math.min(u1, u2, u3);
    if (dp[i] === u1) a++;
    if (dp[i] === u2) b++;
    if (dp[i] === u3) c++;
  }
  return dp[n - 1];
};