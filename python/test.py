class Solution:
    def solveNQueens(self, n: int):

        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board


        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        row = ["."] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        backtrack(0)
        return solutions


s = Solution()

#print(s.solveNQueens(4))

# res = []
# path = [1, 2, ['a', 'b']]
# res.append(path)
# print("path: " , path)
# print("res: " , res)
# print("-------------------")
# path.append(3)
# print("path: " , path)
# print("res: " , res)
# print("-------------------")
# path.pop()
# path[2].append('b')
# print("path: " , path)
# print("res: " , res)
# print("-------------------")
# path[2].pop()
# print("path: " , path)
# print("res: " , res)
# print("-------------------")


from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def check(i, j, k):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        res = False
        visited.add((i, j))
        for diret_i, direct_j in directions:
            next_i, next_j = i + diret_i, j + direct_j
            if 0 <= next_i < height and 0 <= next_j < width:
                if (next_i, next_j) not in visited:
                    if check(next_i, next_j, k + 1):
                        res = True
                        break
        visited.remove((i, j))
        return res

    visited = set()
    height, width = len(board), len(board[0])
    for i in range(height):
        for j in range(width):
            if check(i, j, 0):
                return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
words = ["ABCCED", "SEE", "ABCB"]
for word in words:
    print(exist(board, word))