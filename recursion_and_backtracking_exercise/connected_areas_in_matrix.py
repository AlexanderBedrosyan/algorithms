def find_nested_areas(row, col, rows, columns, matrix):
    if row < 0 or col < 0 or row == rows or col == columns:
        return 0
    if matrix[row][col] == 'A':
        return 0
    if matrix[row][col] == '*':
        return 0

    size = 1
    matrix[row][col] = 'A'

    size += find_nested_areas(row + 1, col, rows, columns, matrix)
    size += find_nested_areas(row, col + 1, rows, columns, matrix)
    size += find_nested_areas(row - 1, col, rows, columns, matrix)
    size += find_nested_areas(row, col - 1, rows, columns, matrix)

    return size


rows = int(input())
columns = int(input())
matrix = []

for row in range(rows):
    matrix.append([ch for ch in input()])

all_areas = {}

for row in range(rows):
    for col in range(columns):
        if matrix[row][col] == '*' or matrix[row][col] == 'A':
            continue
        size = find_nested_areas(row, col, rows, columns, matrix)
        all_areas[f'({row}, {col})'] = size

sorted_areas = dict(sorted(all_areas.items(), key=lambda x: -x[1]))

print(f"Total areas found: {len(sorted_areas)}")
counter = 0
for position, size in sorted_areas.items():
    counter += 1
    print(f"Area #{counter} at {position}, size: {size}")
