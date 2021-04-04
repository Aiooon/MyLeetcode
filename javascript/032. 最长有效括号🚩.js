/* 32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

示例 3：
输入：s = ""
输出：0

提示：
0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'

date: 2021年4月3日 
*/

/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
    /* 思路：栈
    栈中存储的是下标，而不是对应的字符
    初始化：-1 入栈（保持栈底元素保存是当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」）
    当遇到左括号 ( 将它的坐标入栈
    当遇到右括号 ) ，先将栈顶元素弹出，表示匹配了当前括号
        若栈为空，则表示当前括号为没有匹配的右括号，将它的坐标入栈
        若不为空，则表示匹配成功，当前的坐标减去栈顶的坐标即为「以该右括号为结尾的最长有效括号的长度」
    */
    let stack = [];
    let n = s.length, max_len = 0;
    if (n == 0) return 0;
    stack.push(-1);
    for (let i = 0; i < n; i++) {
        if (s[i] == '(') {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.length == 0) {
                stack.push(i);
            } else {
                max_len = Math.max(max_len, i - stack[stack.length - 1]);
            }
        }
    }
    return max_len;
};

s = "(())()";
console.log(longestValidParentheses(s));
