def dfs(node, end_node, graph, final_list, current_list):
    if node not in graph:
        current_list.pop()
        return

    current_list.append(node)

    if end_node in graph[node]:
        current_list.append(end_node)
        final_list.append(current_list)
        return

    for current_node in graph[node]:
        dfs(current_node, end_node, graph, final_list, current_list)

    return final_list

n = int(input())
edges = int(input())

graph = {}

for _ in range(edges):
    start_point, end_point = input().split(' ')
    if start_point not in graph:
        graph[start_point] = []

    graph[start_point].append(end_point)

start_node = input()
end_node = input()
final_list = []

final_list = dfs(start_node, end_node, graph, final_list, [])
result = list(sorted(final_list, key=lambda x: len(x)))[0]
print(f"Shortest path length is: {len(result) - 1}")
print(' '.join(result))
