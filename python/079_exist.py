"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    :param board
    :param word
    :return: bool
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0),]

    def check(i: int, j: int, k: int):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        visited.add((i, j))
        res = False
        for direct_i, direct_j in directions:
            next_i, next_j = i + direct_i, j + direct_j
            if 0 <= next_i < height and 0 <= next_j < width:
                if (next_i, next_j) not in visited:
                    if check(next_i, next_j, k + 1):
                        res = True
                        break
        visited.remove((i, j))
        return res

    height, width = len(board), len(board[0])
    visited = set()
    for i in range(height):
        for j in range(width):
            if check(i, j, 0):
                return True

    return False


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
words = ["ABCCED", "SEE", "ABCB"]
for word in words:
    print(exist(board, word))

