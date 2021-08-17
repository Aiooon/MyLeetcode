/**
 * @param {string} s
 * @return {string[]}
 */
var permutation = function (s) {
  const len = s.length;
  const chars = Array.from(s).sort();
  let visited = new Array(len).fill(false);
  let res = [];

  const backtrack = function (index, path) {
    if (index === len) {
      res.push(path);
      return null;
    }
    for (let i = 0; i < len; i++) {
      if (visited[i] || i > 0 && chars[i] === chars[i - 1] && !visited[i - 1]) {
        continue;
      }
      visited[i] = true;
      backtrack(index + 1, path + chars[i]);
      visited[i] = false;
    }
  }
  backtrack(0, '');
  return res;
};

let s = "aabb"
console.log(permutation(s));
// console.log('');