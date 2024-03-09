def find_path(row, col, board, counter):
    # Base Cases should return number, because the result must add numbers

    if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
        return 0

    if board[row][col] == 'Final':
        return 1

    if board[row][col] == 'A':
        return 0

    # Pre-action

    board[row][col] = 'A'
    result = 0

    # Recursive Call

    result += find_path(row + 1, col, board, counter)
    result += find_path(row, col + 1, board, counter)

    # Post-action
    board[row][col] = '-'

    return result


rows = int(input())
columns = int(input())
board = []

for _ in range(rows):
    board.append(['-' for _ in range(columns)])

board[rows - 1][columns - 1] = 'Final'

print(find_path(0, 0, board, 0))
