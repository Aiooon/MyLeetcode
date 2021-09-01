/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let left = 0, right = 0;
  let window = new Map();
  let res = 0;
  while(right < s.length) {
    let c = s[right];
    right++;
    window.set(c, window.has(c) ? window.get(c) + 1 : 1)
    while(window.get(c) > 1){
      let d = s[left];
      left++;
      window.set(d, window.get(d) - 1);
    }
    res = Math.max(res, right - left);
  }
  return res;
};

console.log(lengthOfLongestSubstring("abcabcbb"));