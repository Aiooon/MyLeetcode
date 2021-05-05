/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    let res = 0;
    while(x !== 0) {
        res = res * 10 + (x % 10);
        x = ~~(x / 10);
        if (res < - (2**31) || res > 2**31 - 1) {
            return 0;
        }
    }
    return res;
};

console.log(reverse(-123));
