/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    s = s.trim();
    let sign = false;
    if (s[0] === '-') {
        sign = true;
    }
    let max = 2**31 - 1, min = -(2**31);
    let num = 0;
    let i = (sign || s[0]==='+') ? 1 : 0;
    while(s[i] !== ' ' && !isNaN(Number(s[i]))){
        num = num * 10 + Number(s[i]);
        i++;
    }
    if (sign) num *= -1;
    if (num < min){
        num = min;
    } else if (num > max) {
        num = max;
    }
    return num;
};


let s = "+1"
console.log(myAtoi(s));
