/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  return s.split(' ').filter((item)=>item !== '').reverse().join(' ');
};

let s = "a  b c."
console.log(s.split(' '));
console.log(s.split(' ').filter((item)=>item !== ''));