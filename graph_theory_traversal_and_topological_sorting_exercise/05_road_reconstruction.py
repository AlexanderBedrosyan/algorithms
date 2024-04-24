def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return

    for child in graph[node]:
        dfs(child, destination, graph, visited)


def find_path(node, destination, graph):
    visited = set()

    dfs(node, destination, graph, visited)

    return destination in visited


number_of_buildings = int(input())
n = int(input())
graph = {}
all_combinations = []

for _ in range(n):
    elements = input().split(' - ')
    if elements[0] not in graph:
        graph[elements[0]] = []
    if elements[1] not in graph:
        graph[elements[1]] = []
    graph[elements[0]].append(elements[1])
    graph[elements[1]].append(elements[0])
    all_combinations.append((elements[0], elements[1]))
    all_combinations.append((elements[1], elements[0]))

final_list = []

for node, destination in sorted(all_combinations, key=lambda t: (t[0], t[1])):
    if node not in graph[destination] or destination not in graph[node]:
        continue

    graph[node].remove(destination)
    graph[destination].remove(node)

    if not find_path(node, destination, graph):
        final_list.append((node, destination))
    else:
        graph[node].append(destination)
        graph[destination].append(node)

print(f"Important streets:")
for elements in final_list:
    print(f"{elements[0]} {elements[1]}")
