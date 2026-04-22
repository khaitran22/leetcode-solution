def solveNQueens(n):

    queen = 'Q'
    final_results = []
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    sum_r_and_c = {i: set() for i in range(2*n - 1)}
    diff_r_and_c = {i: set() for i in range(1-n, n)}
    board = []
    for j in range(n):
        board.append(['.' for _ in range(n)])

    def solve(board, placed_queens_num, idx_r, rows, cols, sum_r_and_c, diff_r_and_c):
        if placed_queens_num == n:
            final_results.append(["".join(r) for r in board])
            return True

        for idx_c in range(n):
            if len(rows[idx_r]) == 0 and len(cols[idx_c]) == 0 and len(sum_r_and_c[idx_r+idx_c]) == 0 and len(diff_r_and_c[idx_r-idx_c]) == 0:
                board[idx_r][idx_c] = queen

                rows[idx_r].add(queen)
                cols[idx_c].add(queen)
                sum_r_and_c[idx_r+idx_c].add(queen)
                diff_r_and_c[idx_r-idx_c].add(queen)
                placed_queens_num += 1

                if solve(board, placed_queens_num, idx_r+1, rows, cols, sum_r_and_c, diff_r_and_c):
                    if idx_r == 0:
                        board = []
                        for j in range(n):
                            board.append(['.' for _ in range(n)])
                        rows = [set() for _ in range(n)]
                        cols = [set() for _ in range(n)]
                        sum_r_and_c = {i: set() for i in range(2*n - 1)}
                        diff_r_and_c = {i: set() for i in range(1-n, n)}
                        placed_queens_num = 0
                        return

                board[idx_r][idx_c] = "."
                rows[idx_r].remove(queen)
                cols[idx_c].remove(queen)
                sum_r_and_c[idx_r+idx_c].remove(queen)
                diff_r_and_c[idx_r-idx_c].remove(queen)
                placed_queens_num -= 1

    solve(board, 0, 0, rows, cols, sum_r_and_c, diff_r_and_c)
    return final_results


for n in range(1, 10):
    print(len(solveNQueens(n)))
