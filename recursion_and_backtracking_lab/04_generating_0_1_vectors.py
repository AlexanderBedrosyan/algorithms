def generate_all_combinations(ind, line):
    if ind == len(line):
        print(''.join(str(ch) for ch in line))
        return
    for i in range(2):
        line[ind] = i
        generate_all_combinations(ind + 1, line)


num = int(input())
line = [None] * num

generate_all_combinations(0, line)
