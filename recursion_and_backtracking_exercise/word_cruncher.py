def find_all_combinations(ind, index_of_elements, needed_word, all_elements, new_word, counter_elements):
    if ind == len(needed_word):
        print(' '.join(all_elements))
        return

    if ind not in index_of_elements:
        return

    for element in index_of_elements[ind]:
        if counter_elements[element] == 0:
            continue
        new_word += element
        if new_word == needed_word[0:len(new_word)]:
            all_elements.append(element)
            counter_elements[element] -= 1
            find_all_combinations(ind + len(element), index_of_elements, needed_word, all_elements, new_word, counter_elements)

            new_word = new_word[0:len(new_word) - len(all_elements[-1])]
            counter_elements[element] += 1
            all_elements.pop()


elements = input().split(', ')
needed_word = input()
index_of_elements = {}
counter_elements = {}

for el in elements:

    if el not in counter_elements:
        counter_elements[el] = 0

    counter_elements[el] += 1

    ind = 0

    while True:
        if el not in needed_word[ind:]:
            break

        current_ind = needed_word.index(el, ind)

        if current_ind not in index_of_elements:
            index_of_elements[current_ind] = []

        if el in index_of_elements[current_ind]:
            ind = current_ind + len(el)
            continue
        index_of_elements[current_ind].append(el)

        ind = current_ind + len(el)


find_all_combinations(0, index_of_elements, needed_word, [], '', counter_elements)
