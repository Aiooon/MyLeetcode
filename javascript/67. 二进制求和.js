/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let res = "";
    let carry = 0;
    for (let i = a.length-1, j = b.length-1; i >= 0 || j >= 0; i--, j--) {
        let sum = carry;
        sum += i >= 0 ? parseInt(a[i]) : 0;
        sum += j >= 0 ? parseInt(b[j]) : 0;
        res += sum % 2;
        carry = Math.floor(sum / 2);
    }
    res += carry == 1 ? carry : "";
    return res.split('').reverse().join('');
};

let a = "11", b = "1";
console.log(addBinary(a, b));