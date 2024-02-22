my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)

for i in range(1, n):
    for j in range(i - 1, 0, -1):
        if my_array[j] < my_array[j - 1]:
            my_array[j], my_array[j - 1] = my_array[j - 1], my_array[j]
        else:
            break


print("Sorted array:", my_array)