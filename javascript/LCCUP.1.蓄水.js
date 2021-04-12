/**
 * @param {number[]} bucket
 * @param {number[]} vat
 * @return {number}
 */

/* 
思路： 
因为前面不管怎么升级水桶，后来倒水都是同时倒
所以直接遍历可能的倒水次数，最多倒 max(vat)+1 次
如果需要倒 i 次水， 那么 j 桶容量就要达到 ceil(vat[j] / i)，这个值减去初始的容量 bucket[j] 就是当前桶需要升级的次数

date: 2021年4月11日
*/
var storeWater = function(bucket, vat) {
    if (Math.max(...vat) == 0) {
        return 0;
    }
    let n = bucket.length;
    let max = 10**4;
    let res = 10**4 + n;
    for (let i = 1; i < max; i++) {
        let cur = i;
        for (let j = 0; j < n; j++){
            cur += Math.max(0, Math.ceil(vat[j] / i) - bucket[j]);
        }
        res = Math.min(res, cur);
    }
    return res;
};

var bucket = [0], vat = [1];
console.log(storeWater(bucket, vat));