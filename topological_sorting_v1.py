def find_node_without_dependencies(elements_counter):
    for key, value in elements_counter.items():
        if value == 0:
            return key

    return None


n = int(input())
graph = {}
elements_counter = {}

for _ in range(n):
    information = input().split('->')
    left_element = information[0].rstrip()
    right_element = None
    if len(information) > 1:
        right_element = information[1].lstrip()
        if ',' in right_element:
            right_element = right_element.split(', ')
        else:
            right_element = [right_element]

    graph[left_element] = right_element

    if left_element not in elements_counter:
        elements_counter[left_element] = 0

    if right_element[0] == '':
        continue

    for element in right_element:
        if element not in elements_counter:
            elements_counter[element] = 0
        elements_counter[element] += 1

dependencies = find_node_without_dependencies(elements_counter)
final_list = []

while dependencies and len(elements_counter) > 0:

    node_to_remove = find_node_without_dependencies(elements_counter)

    if not node_to_remove:
        print('Invalid topological sorting')
        exit()

    for child in graph[node_to_remove]:
        if child in elements_counter:
            elements_counter[child] -= 1

    final_list.append(node_to_remove)
    del elements_counter[node_to_remove]

if len(final_list) == 0:
    print('Invalid topological sorting')
    exit()

print(f"Topological sorting: {', '.join(final_list)}")


# Input looks like:
# 6
# A -> B, C
# B -> D, E
# C -> F
# D -> C, F
# E -> D
# F ->
