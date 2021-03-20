/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    if (tokens.length == 0){
        return 0;
    }
    let stack = new Array();
    for (token of tokens){
        if (['+', '-', '*', '/'].includes(token)) {
            num1 = stack.pop();
            num2 = stack.pop();
            if (token == '+') {
                stack.push(num1 + num2);
            } else if (token == '-') {
                stack.push(num2 - num1);
            } else if (token == '*') {
                stack.push(num1 * num2);
            } else {
                stack.push(parseInt(num2 / num1));
            }
        } else {
            stack.push(parseInt(token));
        }
    }
    return stack.pop();
};

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"];
console.log(evalRPN(tokens));