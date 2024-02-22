my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
is_sorted = False

for i in range(n-1):
    is_sorted = True  # При всеки нов елемент се смята, че е сортиран, докато не се извърши swap операция на 10 ред
    for j in range(n-i-1):  # Причината да е n-i-1, защото след всяка итерация последният елемент ще е нагласен,
        # няма смисъл да се проверява
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            is_sorted = False  # ако има swap операция значи не е все още сортиран списъкът
    if is_sorted:  # Ако не е имало swap операция, то значи списък вече е сортиран
        break

print("Sorted array:", my_array)
