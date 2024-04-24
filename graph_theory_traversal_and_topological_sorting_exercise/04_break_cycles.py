def dfs(node1, node2, graph, visited):
    if node1 in visited:
        return

    visited.add(node1)

    if node1 == node2:
        return

    for node in graph[node1]:
        dfs(node, node2, graph, visited)


def path(node1, graph, node2):
    visited = set()

    dfs(node1, node2, graph, visited)

    return node2 in visited




n = int(input())
graph = {}
all_combinations = []

for _ in range(n):
    elements = input().split(' -> ')
    graph[elements[0]] = elements[1].split()
    for child in graph[elements[0]]:
        all_combinations.append((elements[0], child))

sorted_combinations = list(sorted(all_combinations, key=lambda x: (x[0], x[1])))
final_list = []

for node1, node2 in sorted_combinations:
    if node2 not in graph[node1] or node1 not in graph[node2]:
        continue

    graph[node1].remove(node2)
    graph[node2].remove(node1)

    if path(node1, graph, node2):
        final_list.append((node1, node2))
    else:
        graph[node1].append(node2)
        graph[node2].append(node1)

print(f'Edges to remove: {len(final_list)}')
[print(f'{source} - {destination}') for source, destination in final_list]