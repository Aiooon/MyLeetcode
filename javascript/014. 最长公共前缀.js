/* 
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成

date：2021年3月24日
*/

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let len = strs.length;
    
    if (len == 0) {
        return "";
    } else if (len == 1) {
        return strs[0];
    }

    let common_pre = strs[0];
    let common_len = common_pre.length;
    for (let i = 1; i < len; i++) {
        let cur_str = strs[i]
        common_len = Math.min(common_len, cur_str.length);
        let end = 0;
        while (end < common_len && common_pre[end] === cur_str[end]){
            end++;
        }
        if (end == 0){
            return "";
        }
        common_pre = common_pre.slice(0, end);
    }
    return common_pre;
};

// strs = ["flower","flow","flight"];
// strs = ["flower","flow","floight"];
strs = ["dog","racecar","car"]
console.log(longestCommonPrefix(strs));