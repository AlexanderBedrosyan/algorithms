def dfs(node, graph, visited):
    # BASE CASE
    if node in visited:
        return

    # Pre-action
    visited.add(node)

    for child in graph[node]:
        # Recursive call
        dfs(child, graph, visited)

    # Post action
    print(node, end=' ')


graph = {
    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    7: [1],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: []
}

visited = set()

for node in graph:
    dfs(node, graph, visited)