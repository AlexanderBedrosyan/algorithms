def dfs(node, graph, information):
    if len(graph[node]) == 0:
        information[node] = 1
        return 1

    result = 0

    for child in graph[node]:
        if child in information:
            result += information[child]
            continue
        result += dfs(child, graph, information)

    return result


graph = {}
n = int(input())

for i in range(n):
    line = [ch for ch in input()]
    holder = []
    for index, j in enumerate(line):
        if j == 'Y':
            holder.append(index)

    graph[i] = holder

information = {}


for key in graph.keys():
    result = dfs(key, graph, information)
    if key not in information:
        information[key] = result

print(sum(information.values()))
