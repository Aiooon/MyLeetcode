"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明: 你可以假设字符串只包含小写字母。
"""
from collections import defaultdict

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    map_dict = defaultdict(int)
    for c in s:
        map_dict[c] += 1
    for c in t:
        if map_dict[c] == 0:
            return False
        else:
            map_dict[c] -= 1
    # print(map_dict.values())
    for i in map_dict.values():
        if i != 0:
            return False
    return True


s = "anagram"
t = "nagaram"
arr1 = list(s)
arr2 = list(t)
# print(sorted(arr1) == sorted(arr2))
print(isAnagram(s, t))
