class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        tempList = []
        lenList = []
        for c in s:
            if c not in tempList:
                tempList.append(c)
            else:
                lenList.append(len(tempList))
                i = tempList.index(c)
                tempList = tempList[i + 1:]
                tempList.append(c)
        lenList.append(len(tempList))
        return max(lenList) if lenList else 0

    def slipWindow(self, s) -> int:
        hashmap = {}
        # start = end = ans = 0
        # for end in range(len(s)):
        #     if s[end] in hashmap:
        #         start = max(hashmap.get(s[end]), start)
        #     ans = max(end - start + 1, ans)
        #     hashmap.


str = "abcabcdebb"
s = Solution()
length = s.lengthOfLongestSubstring(str)
print(length)