/* 633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。

示例 1：
输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

示例 2：
输入：c = 3
输出：false

示例 3：
输入：c = 4
输出：true

示例 4：
输入：c = 2
输出：true

示例 5：
输入：c = 1
输出：true

提示：

0 <= c <= 2^31 - 1

date: 2021年4月28日*/

/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function (c) {
    let left = 0, right = parseInt(Math.sqrt(c));
    while(left <= right){
        let num = left**2 + right**2;
        if (num == c) {
            return true;
        } else if (num < c){
            left++;
        } else {
            right--;
        }
    }
    return false;
};

console.log(judgeSquareSum(2));