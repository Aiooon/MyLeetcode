/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    let res = [];
    dfs('', n, n, res);
    return res;
};

var dfs = function (sol, left, right, res) {
    if (left == 0 && right == 0) {
        res.push(sol);
        return;
    }
    if (left > right) return;
    if (left > 0) dfs(sol + '(', left - 1, right, res);
    if (right > 0) dfs(sol + ')', left, right - 1, res);
}

console.log(generateParenthesis(2));