def recursive_fibonacci(n, list):
    if len(list) == n + 1:
        print(list[n])
        return
    new_number = list[-1] + list[-2]
    list.append(new_number)
    recursive_fibonacci(n, list)


recursive_fibonacci(int(input()), [1, 1])