def isValidSudoku(board) -> bool:
    is_valid = True
    # check row
    for row in board:
        hash_map = {}
        for cell in row:
            if cell != ".":
                if hash_map.get(cell) == None:
                    hash_map[cell] = 1
                else:
                    return False

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

    return is_valid
