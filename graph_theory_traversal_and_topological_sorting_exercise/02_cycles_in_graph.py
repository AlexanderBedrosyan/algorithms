def dfs(node, graph, visited):
    if node in visited:
        print("Acyclic: No")
        exit()

    if node not in graph:
        print(f"Acyclic: Yes")
        exit()

    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)


graph = {}

while True:
    command = input()

    if command == 'End':
        break

    start, end = command.split('-')

    if start not in graph:
        graph[start] = []

    graph[start].append(end)


visited = set()


for key in graph.keys():
    dfs(key, graph, visited)
