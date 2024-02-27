# Solution 1
numbers = list(map(int, input().split()))


def calculate_sum(ind, total_amount):
    total_amount += numbers[ind]
    if ind == (len(numbers) - 1):
        return total_amount
    ind += 1

    return calculate_sum(ind, total_amount)


print(calculate_sum(0, 0))


# Solution 2
def array_sum(arr, idx):
    if idx >= len(arr) - 1:
        return arr[idx]
    return arr[idx] + array_sum(arr, idx + 1)


array = [int(x) for x in input().split()]

print(array_sum(array, 0))
