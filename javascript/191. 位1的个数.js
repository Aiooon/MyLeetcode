/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let res = 0;
    while(n) {
        res++;
        n &= (n-1)
    }
    return res;
};

n = 00000000000000000000000000001011
console.log(hammingWeight(n));
