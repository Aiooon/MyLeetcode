/* 
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

date：2021年4月15日
*/

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
    let map = new Map();
    for (const s of strs) {
        let key = Array.from(s).sort().toString();
        let list = map.get(key) ? map.get(key) : new Array();
        list.push(s);
        map.set(key, list);
    }
    return Array.from(map.values());
};

// console.log(Array.from("bca").sort().toString());

var strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(groupAnagrams(strs));