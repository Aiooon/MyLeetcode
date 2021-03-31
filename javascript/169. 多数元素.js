/**
 * @param {number[]} nums
 * @return {number}
 */

// 时间：O(N)  空间：O(N)
// var majorityElement = function(nums) {
//     let map = new Map();
//     for (num of nums) {
//         if (map.has(num)) {
//             map.set(num, map.get(num) + 1)
//             if(map.get(num) > (nums.length / 2)) return num;
//         } else {
//             map.set(num, 1);
//         }
//     }
// };

// Boyer-Moore 投票算法
var majorityElement = function(nums) {
    let candidate = null;   // 候选众数
    let count = 0;  // 候选众数出现的次数
    for (num of nums) {
        // 当这个候选出现的次数为 0 时，将当前的 num 设为候选
        if (count == 0) candidate = num;
        if (num != candidate) {   // 如果当前的数不等于候选，count--
            count--;
        } else {    // 如果相等则 count++
            count++;
        }
    }
    return candidate;
}
let nums = [2,2,1,1,1,2,2]
console.log(majorityElement(nums));