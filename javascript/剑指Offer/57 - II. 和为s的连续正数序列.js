/**
 * @param {number} target
 * @return {number[][]}
 */
var findContinuousSequence = function (target) {
  let i = 1, j = 2;
  let s = 3;
  let window = [1, 2], res = [];
  while(i < j) {
    if (s === target) {
      res.push(window.slice());
    }
    if (s >= target) {
      window.shift();
      s -= i;
      i++;
    } else {
      j++;
      window.push(j);
      s += j;
    }
  }
  return res;
};

console.log(findContinuousSequence(9));