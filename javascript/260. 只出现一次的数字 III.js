/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function (nums) {
    let ret = 0;    // ret 保存所有数字异或后的结果
    let a = 0, b = 0;  // a，b 保存结果
    for (num of nums) {
        ret ^= num;
    }
    let h = 1;
    while ((ret & h) === 0) {   // 找到异或结果中第一个 1 的位置
        h <<= 1;
    }
    for (num of nums) {
        if (num & h) {
            a ^= num;
        } else {
            b ^= num;
        }
    }
    return [a, b];
};

nums = [1, 2, 1, 3, 2, 5]
console.log(singleNumber(nums));
let h = 1;
console.log(6 & h)
if ((6 & h) == 0) {
    console.log("true");
}
// while (ret & h === 0) {   // 找到异或结果中第一个 1 的位置
//     h <<= 1;
// }