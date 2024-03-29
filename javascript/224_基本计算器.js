/* 224. 基本计算器
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

提示：
1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

date: 2021年3月10日
 */

/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
    const ops = [1];
    let res = 0;
    let sign = 1;
    let i = 0;
    const l = s.length;
    while (i < l){
        if (s[i] === ' '){
            i++;
        } else if (s[i] === '+'){
            sign = ops[ops.length - 1];
            i++;
        } else if (s[i] === '-'){
            sign = -ops[ops.length - 1];
            i++;
        } else if (s[i] === '('){
            ops.push(sign);
            i++;
        } else if (s[i] === ')'){
            ops.pop();
            i++;
        } else {
            let num = 0;
            while (i < l && !(isNaN(Number(s[i]))) && s[i] !== ' '){
                num = num * 10 + s[i].charCodeAt() - '0'.charCodeAt();
                i++;
            }
            res += sign * num
        }
    }
    return res
};

var s = "-(1 + 2 - (3 + 4))"
console.log(calculate(s))
// console.log('123'.charCodeAt())