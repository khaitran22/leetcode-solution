def solveNQueens(n):

    queen = 'Q'

    def valid():
        pass

    def solve(board, placed_queens_num):

        if placed_queens_num == n:
            return True

        for idx_r, r in enumerate(board):
            for idx_c, c in enumerate(board):
                if len(rows[idx_r]) == 0 and len(cols[idx_c]) == 0 and len(sum_r_and_c[r+c]) == 0 and len(diff_r_and_c[r-c]) == 0:
                    board[r][c] = queen

                    rows[idx_r].add(queen)
                    cols[idx_c].add(queen)
                    sum_r_and_c[r+c].add(queen)
                    diff_r_and_c[r-c].add(queen)
                    placed_queens_num += 1

                    if solve(board, placed_queens_num):
                        return True
                    else:
                        rows[idx_r].remove(queen)
                        cols[idx_c].remove(queen)
                        sum_r_and_c[r+c].remove(queen)
                        diff_r_and_c[r-c].remove(queen)
                        placed_queens_num -= 1

    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    sum_r_and_c = {i: set() for i in range(2*n - 2)}
    diff_r_and_c = {i: set() for i in range(1-n, n)}

    board = []
    for j in range(n):
        board.append(['.' for _ in range(n)])
    solve(board, 0)

    return board


n = 5
solveNQueens(n)
