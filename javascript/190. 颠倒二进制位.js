/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
/* 位运算符将它的操作数视为32位元的二进制串（0和1组成）而非十进制八进制或十六进制数。
例如：十进制数字9用二进制表示为1001，位运算符就是在这个二进制表示上执行运算，
但是返回结果是标准的JavaScript数值。
 */
var reverseBits = function(n) {
    let res = 0;
    for (let i = 0; i < 32; i++) {
        res = (res << 1) + (n & 1);
        n >>= 1;
    }
    return res >>> 0;   // 开头补 0
};

