/**
 * @param {number} n
 * @return {boolean}
 */
//  丑数 就是只包含质因数 2、3 和/或 5 的正整数。
var isUgly = function (n) {
    if (n <= 0) {
        return false;
    }
    const factors = [2, 3, 5];
    for (const factor of factors) {
        while (n % factor === 0) {
            n /= factor;
        }
    }
    return n == 1;
};

console.log(isUgly(10));