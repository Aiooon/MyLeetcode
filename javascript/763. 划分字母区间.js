/*
763. 划分字母区间
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

提示：
S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。
date: 2021年6月4日
*/
/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function (s) {
    const n = s.length;
    let last = new Array(26);   // 记录每个字母最后出现的位置
    const codea = 'a'.codePointAt(0);
    for (let i = 0; i < n; i++) {
        last[s.codePointAt(i) - codea] = i;
    }
    let partition = [];
    let end = 0, start = 0;
    for (let i = 0; i < n; i++) {
        end = Math.max(end, last[s.codePointAt(i) - codea]);
        if (i === end) {
            partition.push(end - start + 1);
            start = end + 1;
        }
    }
    return partition;
};

s = 'ababcbacadefegdehijhklij'
console.log(partitionLabels(s));
// console.log('ab'.codePointAt(1));