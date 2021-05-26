/**
 * @param {string} s
 * @return {string}
 */
var reverseParentheses = function (s) {
    let stack = [""];
    for (const c of s) {
        if (c === '(') {
            stack.push("");
        } else if (c === ')'){
            let cur = stack.pop();
            cur = cur.split('').reverse().join('');
            stack.push(stack.pop() + cur);
        } else {
            stack.push(stack.pop() + c);
        }
    }
    return stack.toString();
};

s = "a(bcd(mno)p)q";    // a p mno dcb q
console.log(reverseParentheses(s));