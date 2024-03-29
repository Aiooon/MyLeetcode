/*
12. 整数转罗马数字
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。
12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如 4 不写做 IIII，而是 IV。
数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:
输入: 3
输出: "III"

示例 2:
输入: 4
输出: "IV"

示例 3:
输入: 9
输出: "IX"

示例 4:
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

示例 5:
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.

提示：1 <= num <= 3999

date: 2021年3月23日
 */
/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
    let i = 0, res = '';
    const nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    const romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    while (i < 13) {
        while (num >= nums[i]) {
            res += romans[i];
            num -= nums[i];
        }
        i++;
    }
    return res;
};


/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
    const vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    let val2syb = new Map();
    val2syb.set(1000, "M");
    val2syb.set(900, "CM");
    val2syb.set(500, "D");
    val2syb.set(400, "CD");
    val2syb.set(100, "C");
    val2syb.set(90, "XC");
    val2syb.set(50, "L");
    val2syb.set(40, "XL");
    val2syb.set(10, "X");
    val2syb.set(9, "IX");
    val2syb.set(5, "V");
    val2syb.set(4, "IV");
    val2syb.set(1, "I");
    let ans = [];
    for (const val of vals) {
        syb = val2syb.get(val);
        while (num >= val) {
            num -= val;
            ans.push(syb);
        }
        if (num == 0) {
            break;
        }
    }
    return ans.join('');
};






num = 1994
console.log(intToRoman(num));