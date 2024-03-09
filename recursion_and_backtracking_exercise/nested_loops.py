def loops_to_recursion(num, array):
    # BASE CASE
    if len(array) == num:
        print(' '.join(str(ch) for ch in array))
        return

    # Pre-action
    for i in range(1, num + 1):
        array.append(i)
        # Recursive call
        loops_to_recursion(num, array)

        # Post-action
        array.pop()


loops_to_recursion(int(input()), [])
