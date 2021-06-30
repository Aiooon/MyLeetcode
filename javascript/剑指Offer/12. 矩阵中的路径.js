/* 
剑指 Offer 12. 矩阵中的路径
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

提示：
1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成

注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/

date：2021年6月30日
*/

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {
    /* 
    思路：深度优先搜索/回溯/剪枝
    */
    // i, j 表示当前遍历元素的坐标，k 表示当前目标字符在 word 中的索引
    const row = board.length, col = board[0].length;
    const len = word.length;
    var dfs = function (i, j, k) {
        if (!(0 <= i && i < row) || !(0 <= j && j < col) || board[i][j] !== word[k]) {
            return false;
        }
        if (k === len - 1) {
            return true;
        }
        board[i][j] = ' ';
        let res = dfs(i - 1, j, k + 1) || dfs(i, j - 1, k + 1) || dfs(i + 1, j, k + 1) || dfs(i, j + 1, k + 1);
        board[i][j] = word[k];  // 这里在还原 board[i][j] 的值时，因为是在board[i][j] = word[k]的前提下，所以可以直接还原为word[k]
        return res;
    }

    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (dfs(i, j, 0)) {
                return true;
            }
        }
    }
    return false;
};

const board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "ABCCED";
console.log(exist(board, word));