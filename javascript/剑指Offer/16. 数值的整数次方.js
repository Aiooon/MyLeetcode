/* 
剑指 Offer 16. 数值的整数次方
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。不得使用库函数，同时不需要考虑大数问题。

示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000

示例 2：
输入：x = 2.10000, n = 3
输出：9.26100

示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25

提示：
-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= x^n <= 10^4

注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/

date: 2021年7月8日
*/

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function (x, n) {
    if (n === 0) {
        return 1;
    }
    if (n === 1) {
        return x;
    }
    if (n === -1) {
        return 1 / x;
    }
    if (n % 2 === 0) {
        const a = myPow(x, n / 2)
        return a * a;
    } else {
        const b = myPow(x, (n - 1) / 2);
        return b * b * x;
    }
};

console.log(myPow(2.00000, -2147483648));