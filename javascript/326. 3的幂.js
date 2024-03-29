/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function (n) {
    if (n <= 0) {
        return false;
    }
    while (n % 3 === 0) {
        n /= 3;
    }
    return n === 1;
    // return n > 0 && 1162261467 % n == 0;
};