// /**
//  * @param {number} n
//  * @return {string[][]}
//  */
// var solveNQueens = function (n) {
//     var board = new Array(n);
//     for (let i = 0; i < n; i++){
//         board[i] = new Array(n);
//         board[i].fill(0)
//     }
//     var res = [];
//     backtrack(res, [], board, 0);  // sol[i] 记录第 i 行棋子的列坐标
//     return res;
// };

// var backtrack = function (res, sol, board, row) {
//     if (sol.length == board.length) {
//         res.push(sol.slice());
//         return
//     }
//     len = board.length;
//     for (let i = 0; i < len; i++) {
//         if (isValid(board, row, i)) {
//             board[row][i] = 1
//             sol.push(i);
//             backtrack(res, sol, board, row + 1);
//             board[row][i] = 0
//             sol.pop();
//         }
//     }

// };

// // 判断棋盘位置 board[row][col] 是否可以放置棋子
// var isValid = function (board, row, col) {
//     var len = board.length
//     // 检查列
//     for (let i = 0; i < len; i++) {
//         if (board[i][col]) return false;
//     }
//     // 检查左上对角线
//     for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
//         if (board[i][j]) return false;
//     }
//     // 检查右上对角线
//     for (let i = row - 1, j = col + 1; i >= 0 && j < len; i--, j++) {
//         if (board[i][j]) return false;
//     }
//     return true;
// };

/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function (n) {
    const board = new Array(n).fill(0).map(() => new Array(n).fill(0));
    let res = [];

    var isValid = (row, col) => {
        // 检查列
        for (let i = 0; i < n; i++) {
            if (board[i][col] === 1) return false;
        }
        // 检查左上对角线
        for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j]) return false;
        }
        // 检查右上对角线
        for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j]) return false;
        }
        return true;
    }

    var backtrack = (row, sol) => {
        if (sol.length === n) {
            res.push(sol.slice());
            return;
        }
        for (let i = 0; i < n; i++) {
            if (isValid(row, i)) {
                board[row][i] = 1;
                sol.push(i);
                backtrack(row + 1, sol);
                board[row][i] = 0;
                sol.pop();
            }
        }
    }

    backtrack(0, [])
    return res;
};

var generateBoard = (sol) => {
    let board = [], size = sol.length;
    for (let i = 0; i < size; i++) {
        let row = new Array(size).fill(".");
        row[sol[i]] = "Q";
        board.push(row.join(''));
    }
    return board;
}

var n = 4
var ans = [[1, 3, 0, 2], [2, 0, 3, 1]];
const res = solveNQueens(n);
console.log(res);
console.log(res.map((sol) => generateBoard(sol)));
[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]