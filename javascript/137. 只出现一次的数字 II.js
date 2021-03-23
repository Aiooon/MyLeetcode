/* 137. 只出现一次的数字 II
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,3,2]
输出: 3
示例 2:

输入: [0,1,0,1,0,1,99]
输出: 99

date: 2021年3月22日
*/


/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let myMap = new Map();
    for(num of nums) {
        if (myMap.has(num)){
            val = myMap.get(num);
            myMap.set(num, ++val);   // todo err
        } else {
            myMap.set(num, 1);
        }
    }
    for (let [key, val] of myMap) {
        if (val === 1) {
            return key;
        }
    }
};

let nums = [0,1,0,1,0,1,99];
console.log(singleNumber(nums));