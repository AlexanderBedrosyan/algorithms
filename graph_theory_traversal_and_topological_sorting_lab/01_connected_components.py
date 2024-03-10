def dfs(node, graph, visited_nodes, components):
    # BASE CASE
    if node in visited_nodes:
        return

    visited_nodes.add(node)

    for child in graph[node]:
        dfs(child, graph, visited_nodes, components)

    components.append(node)


n = int(input())
graph = {}

for i in range(n):
    line = input()
    child = [] if line == '' else [int(x) for x in line.split()]
    graph[i] = child

visited_nodes = set()

for key in graph.keys():
    if key in visited_nodes:
        continue
    components = []
    dfs(key, graph, visited_nodes, components)
    print(f"Connected component: {' '.join(str(ch) for ch in components)}")
