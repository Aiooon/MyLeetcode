/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    if (s.length == 0){
        return 0;
    };
    var numStack = new Array();
    var op = '';
    var i = 0;
    while (i < s.length){
        if (s[i] == ' '){
            i++; 
        } else if (['+', '-', '*', '/'].includes(s[i])) {
            op = s[i];
            i++;
        } else if (!isNaN(s[i])) {
            let num = 0;
            while (i < s.length && !isNaN(parseInt(s[i]))) {
                num = num * 10 + (parseInt(s[i]));
                i += 1
            };
            if (op == '+' || op == '') {
                numStack.push(num)
            } else if (op == '-') {
                numStack.push(-num)
            } else if (op == '*') {
                numStack.push(numStack.pop() * num)
            } else if (op == '/') {
                numStack.push(parseInt(numStack.pop() / num));
            };
        };
    };
    return sum(numStack);
};

function sum(arr) {
    let s = 0;
    for (let i = arr.length-1; i >= 0; i--) {
        s += arr[i];
    }
    return s;
}

let s = " 3/2 ";
console.log(calculate(s));

// console.log(isNaN(parseInt(' ')))