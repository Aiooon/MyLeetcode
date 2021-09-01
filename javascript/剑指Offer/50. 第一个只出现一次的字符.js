/**
 * @param {string} s
 * @return {character}
 */
var firstUniqChar = function (s) {
  let dic = new Map();
  const n = s.length;
  for (let i = 0; i < n; i++) {
    dic.set(s[i], dic.has(s[i]) ? true : false);
  }
  for (let i = 0; i < n; i++) {
    if (dic.get(s[i]) === false) {
      return s[i];
    }
  }
  return ' ';
};