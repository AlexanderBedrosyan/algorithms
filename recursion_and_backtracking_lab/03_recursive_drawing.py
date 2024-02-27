# Solution 1
def recursive_drawing_positive(n):
    if n == 0:
        return
    print(n * '*')
    return recursive_drawing_positive(n - 1)


def recursive_drawing_negative(starting_number, end_number):
    if starting_number > end_number:
        return
    print(starting_number * '#')
    return recursive_drawing_negative(starting_number + 1, end_number)


n = int(input())

recursive_drawing_positive(n)
recursive_drawing_negative(1, n)

# Solution 2


def draw_fig(n):
    if n < 1:
        return
    print('*' * n)
    draw_fig(n - 1)
    print('#' * n)


num = int(input())

draw_fig(num)