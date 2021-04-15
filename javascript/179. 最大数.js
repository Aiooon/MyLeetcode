/* 179. 最大数
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：
输入：nums = [1]
输出："1"

示例 4：
输入：nums = [10]
输出："10"

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 109

date: 2021年4月12日
*/

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function (nums) {
    if (Math.max(...nums) == 0){
        return '0';
    }
    nums.sort((a, b) => {
        if (a == b) {
            return 0;
        }
        let sa = 10, sb = 10;
        while (sa <= a) {
            sa *= 10;
        }
        while (sb <= b) {
            sb *= 10;
        }
        let ba = (sa * b + a);
        let ab = (sb * a + b);
        return ba - ab;     // 如果 ba > ab，则 b 在前 a 在后，返回 1
    });
    return nums.join('');
};

var nums = [10,2];
console.log(largestNumber(nums));