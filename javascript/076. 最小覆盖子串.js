/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
  let window = new Map();
  let left = 0, right = 0;
  let need = new Map();
  let valid = 0, start = 0;
  let minlen = Number.MAX_SAFE_INTEGER;
  for (c of t) {
    need.set(c, need.has(c) ? need.get(c) + 1 : 1);
  }
  const n = s.length;
  while (right < n) {
    let c = s[right];
    right++;
    if(need.has(c)){
      window.set(c, window.has(c) ? window.get(c) + 1 : 1);
      if(need.get(c) === window.get(c)) {
        valid++;
      }
    }
    while(valid === need.size) {
      if (right - left < minlen) {
        minlen = right - left;
        start = left;
      }
      let d = s[left];
      left++;
      if (need.has(d)) {
        if (need.get(d) === window.get(d)) {
          valid--;
        }
        window.set(d, window.get(d) - 1);
      }
    }
  }
  return minlen !== Number.MAX_SAFE_INTEGER ? s.slice(start, start + minlen) : "";
};

console.log(minWindow("aa","aa"));