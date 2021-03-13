/**
 * @param {string} preorder
 * @return {boolean}
 */
var isValidSerialization = function(preorder) {
    var stack = [];
    var nodes = preorder.split(',');
    for (node of nodes) {
        stack.push(node);
        while (stack.length >= 3 && stack[stack.length-1] == '#' && stack[stack.length-2] == '#' && stack[stack.length-3] != '#') {
            stack.pop();
            stack.pop();
            stack.pop();
            stack.push('#');
        }
    }
    return stack.length == 1 && stack.pop() == '#'
};


s = "9,3,4,#,#,1,#,#,2,#,6,#,#";
console.log(isValidSerialization(s))