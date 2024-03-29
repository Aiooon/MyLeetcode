"""
剑指 Offer 12. 矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。


示例 1：

输入：
board = [["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]],
word = "ABCCED"
输出：true
示例 2：

输入：
board = [["a","b"],
        ["c","d"]],
word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200

date = 9-29-2020
"""
from typing import List


class Solution:
    # one answer
    def exist_(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            tmp, board[i][j] = board[i][j], '/'
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        """

        :param board:
        :param word:
        :return:
        """
        if not board or not word:
            return False

        def check(row, col, char_index_in_word) -> bool:
            if board[row][col] != word[char_index_in_word]:
                return False
            if char_index_in_word == len(word) - 1:
                return True

            res = False
            visited.add((row, col))
            for row_step, col_step in directions:
                next_row, next_col = row + row_step, col + col_step
                if 0 <= next_row < height and 0 <= next_col < width:
                    if (next_row, next_col) not in visited:
                        if check(next_row, next_col, char_index_in_word + 1):
                            res = True
                            break
            visited.remove((row, col))
            return res

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 计算方向
        visited = set()    # 用set记录走过的格子
        height, width = len(board), len(board[0])

        for i in range(height):
            for j in range(width):
                if check(i, j, 0):
                    return True

        return False


sol = Solution()
board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
words = ["ABCCED", "SEE", "ABCB"]
for word in words:
    print(sol.exist(board, word))