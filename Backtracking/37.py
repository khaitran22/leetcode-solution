def solveSudoku_slow_TLError(board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    total_nums = set([str(i+1) for i in range(9)])

    def isValidSudoku(board):
        # check row
        # for row in board:
        #     hash_map = {}
        #     for cell in row:
        #         if cell != ".":
        #             if hash_map.get(cell) == None:
        #                 hash_map[cell] = 1
        #             else:
        #                 return False

        # check column
        for column in range(9):
            hash_map = {}
            for row in board:
                if row[column] != ".":
                    if hash_map.get(row[column]) == None:
                        hash_map[row[column]] = 1
                    else:
                        return False

        # check cell
        for block in range(3):
            rows = board[block*3: block*3+3]
            for local_column in range(9):
                if local_column % 3 == 0:
                    hash_map = {}
                for row in rows:
                    if row[local_column] != ".":
                        if hash_map.get(row[local_column]) == None:
                            hash_map[row[local_column]] = 1
                        else:
                            return False

        return True

    def isFilled(board):
        for row in board:
            for e in row:
                if e == ".":
                    return False
        return True

    def solve(board, r, c, nums, used, false_boards):
        if isValidSudoku(board) and isFilled(board):
            return True

        cell = board[r][c]
        if cell == ".":
            for left_num in nums:
                board[r][c] = left_num
                check_board = tuple([tuple(r) for r in board])
                if not check_board in false_boards:
                    if isValidSudoku(board):
                        if not isFilled(board):
                            increase = (c+1)//9
                            used[r].add(left_num)
                            outcome = solve(board, r+increase, (c+1) %
                                            9, sorted(total_nums - used[r+increase]), used, false_boards)
                            if not outcome:
                                false_board = tuple([tuple(r) for r in board])
                                if not false_board in false_boards:
                                    false_boards.add(false_board)
                                board[r][c] = "."
                                used[r].remove(left_num)
                            else:
                                return outcome
                        else:
                            return True

                    else:
                        false_board = tuple([tuple(r) for r in board])
                        false_boards.add(false_board)
                        board[r][c] = "."
                        next_nums = [i for i in nums if i != left_num]
                        if len(next_nums) == 0:
                            return False
                        return solve(board, r, c, next_nums, used, false_boards)
                else:
                    board[r][c] = "."
                    outcome = False
            return outcome
        else:
            increase = (c+1)//9
            return solve(board, r+increase, (c+1) %
                         9, sorted(total_nums - used[r+increase]), used, false_boards)

    used = []
    for row in board:
        row_used = set()
        for cell in row:
            if cell != ".":
                row_used.add(cell)
        used.append(row_used)
    false_boards = set()
    solve(board, 0, 0, total_nums, used, false_boards)


def solveSudoku_leetcode_accepted(board):

    # Constraint-checking (used)
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    filled_cells = set([])

    for idx_r, r in enumerate(board):
        for idx_c, c in enumerate(r):
            if c != ".":
                rows[idx_r].add(c)
                cols[idx_c].add(c)
                boxes[(idx_r // 3)*3 + idx_c // 3].add(c)
                filled_cells.add((idx_r, idx_c))

    def solve(board, r, c, filled_cells):

        if len(filled_cells) == 81:
            return True

        if board[r][c] == ".":
            for val in "123456789":
                # Check isValid(board)
                if val not in rows[r] and val not in cols[c] and val not in boxes[(r // 3)*3 + c // 3]:
                    board[r][c] = val

                    # save the current one
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3)*3 + c // 3].add(val)
                    filled_cells.add((r, c))

                    if solve(board, r+((c+1)//9), (c+1) % 9, filled_cells):
                        return True
                    else:
                        # not consider this val anymore
                        board[r][c] = "."
                        rows[r].remove(val)
                        cols[c].remove(val)
                        boxes[(r // 3)*3 + c // 3].remove(val)
                        filled_cells.remove((r, c))
            return False
        else:
            return solve(board, r+((c+1)//9), (c+1) % 9, filled_cells)

    solve(board, 0, 0, filled_cells)


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
result = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
]
solveSudoku_leetcode_accepted(board)
assert board == result
