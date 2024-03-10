def dfs(row, col, matrix, empty_matrix, element):
    if row < 0 or col < 0 or row == len(matrix) or col == len(matrix[0]):
        return

    if empty_matrix[row][col] is True:
        return

    if element != matrix[row][col]:
        return

    empty_matrix[row][col] = True

    dfs(row + 1, col, matrix, empty_matrix, element)
    dfs(row - 1, col, matrix, empty_matrix, element)
    dfs(row, col + 1, matrix, empty_matrix, element)
    dfs(row, col - 1, matrix, empty_matrix, element)


matrix = []
empty_matrix = []

rows = int(input())
columns = int(input())

for _ in range(rows):
    matrix.append([ch for ch in input()])
    empty_matrix.append([None for _ in range(columns)])

information = {}


for row in range(rows):
    for col in range(columns):
        if empty_matrix[row][col] is True:
            continue
        element = matrix[row][col]
        dfs(row, col, matrix, empty_matrix, element)

        if element not in information:
            information[element] = 0
        information[element] += 1

sorted_info = dict(sorted(information.items(), key=lambda x: x))
print(f"Areas: {sum(information.values())}")
for key, value in sorted_info.items():
    print(f"Letter '{key}' -> {value}")
