/* 
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000

date: 2021年6月26日
*/

/**
 * @param {string} s
 * @return {string}
 */
var replaceSpace = function(s) {
    return s.split(' ').join('%20');
};
/* 
执行用时：108 ms, 在所有 JavaScript 提交中击败了   5.16% 的用户
内存消耗：37.4 MB, 在所有 JavaScript 提交中击败了 92.61% 的用户 
*/

var btr_replaceSpace = function(s) {
    s = s.split('');
    let olen = s.length;
    let spaceCount = 0;
    for (let c of s) {
        if (c == ' ') spaceCount++;
    }
    if (spaceCount > 0) {
        s.length += spaceCount * 2
        for (let i = olen - 1, j = s.length - 1; i >= 0; i--, j--) {
            if (s[i] !== ' ') {
                s[j] = s[i];
            } else {
                s[j-2] = '%';
                s[j-1] = '2';
                s[j]   = '0';
                j -= 2;
            }
        }
    }
    return s.join('');
};
/* 
执行用时：88 ms, 在所有 JavaScript 提交中击败了   33.29% 的用户
内存消耗：37.6 MB, 在所有 JavaScript 提交中击败了 59.87% 的用户 */

let s = 'We are happy.'
// console.log(s.split(' ').join('%20'));

