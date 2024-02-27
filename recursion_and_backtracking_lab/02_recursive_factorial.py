def recursive_factorial(number):
    if number == 1:
        return number
    return number * recursive_factorial(number - 1)


print(recursive_factorial(int(input())))