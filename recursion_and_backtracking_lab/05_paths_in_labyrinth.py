def find_the_all_paths(row, col, matrix, direction, path):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return

    if matrix[row][col] == '*':
        return

    if matrix[row][col] == 'e':
        path.append(direction)
        print(''.join(path))
        path.pop()
        return

    if matrix[row][col] == 'A':
        return

    path.append(direction)
    matrix[row][col] = 'A'

    find_the_all_paths(row + 1, col, matrix, 'D', path)
    find_the_all_paths(row - 1, col, matrix, 'U', path)
    find_the_all_paths(row, col + 1, matrix, 'R', path)
    find_the_all_paths(row, col - 1, matrix, 'L', path)

    matrix[row][col] = '-'
    path.pop()


row = int(input())
col = int(input())
matrix = []

for _ in range(row):
    matrix.append([ch for ch in input()])

find_the_all_paths(0, 0, matrix, '', [])
