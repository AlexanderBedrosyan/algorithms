def reverse_array(index, current_array):
    # BASE CASE
    if index >= len(current_array):
        print(' '.join(current_array))
        return

    # Pre-action
    ch = current_array.pop()
    current_array.insert(index, ch)

    # Recursive call
    reverse_array(index + 1, current_array)


lst = input().split(' ')
reverse_array(0, lst)