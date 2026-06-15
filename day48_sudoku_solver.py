from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3 + j//3].add(num)

        def backtrack(i, j):
            if i == 9:
                return True
            if j == 9:
                return backtrack(i+1, 0)
            if board[i][j] != '.':
                return backtrack(i, j+1)
            box_idx = (i//3)*3 + j//3
            for num in map(str, range(1, 10)):
                if num in rows[i] or num in cols[j] or num in boxes[box_idx]:
                    continue
                board[i][j] = num
                rows[i].add(num); cols[j].add(num); boxes[box_idx].add(num)
                if backtrack(i, j+1):
                    return True
                board[i][j] = '.'
                rows[i].remove(num); cols[j].remove(num); boxes[box_idx].remove(num)
            return False

        backtrack(0, 0)

# Test nhanh
if __name__ == "__main__":
    s = Solution()
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(board)
    for row in board:
        print(row)
