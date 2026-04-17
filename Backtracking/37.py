def solveSudoku(board) -> None:
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

    def solve(board, r, c, nums, used):
        if isValidSudoku(board) and isFilled(board):
            return

        if r == 2:
            print("Currently filled board:")
            for t_idx, r1 in enumerate(board):
                print(r1)
                if t_idx == 8:
                    print("-"*20)
            a = 1

        cell = board[r][c]
        if cell == ".":
            for left_num in nums:
                board[r][c] = left_num
                # if board[0][5] == '6':
                #     a = 1
                # print("Currently filled board:")
                # for t_idx, r1 in enumerate(board):
                #     print(r1)
                #     if t_idx == 8:
                #         print("-"*20)
                if isValidSudoku(board):
                    increase = (c+1)//9
                    used[r].add(left_num)
                    outcome = solve(board, r+increase, (c+1) %
                                    9, sorted(total_nums - used[r+increase]), used)
                    if not outcome:
                        board[r][c] = "."
                        used[r].remove(left_num)

                else:
                    board[r][c] = "."
                    next_nums = [i for i in nums if i != left_num]
                    if len(next_nums) == 0:
                        return False
                    outcome = solve(board, r, c, next_nums, used)
            return outcome
        else:
            increase = (c+1)//9
            solve(board, r+increase, (c+1) %
                  9, sorted(total_nums - used[r+increase]), used)

    used = []
    for row in board:
        row_used = set()
        for cell in row:
            if cell != ".":
                row_used.add(cell)
        used.append(row_used)

    solve(board, 0, 0, total_nums, used)


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
solveSudoku(board)
assert board == result
