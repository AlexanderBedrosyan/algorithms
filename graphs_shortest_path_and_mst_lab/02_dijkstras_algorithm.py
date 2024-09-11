def dfs(node, final_city, graph, full_paths, visited, counter, current_distances):
    if node == final_city:
        if full_paths:
            needed_key = sum(full_path.keys())
            if needed_key < counter:
                return
            else:
                del full_paths[needed_key]
                full_paths[counter] = [ch for ch in current_distances]
        else:

            full_paths[counter] = []
            for ch in current_distances:
                full_path[counter].append(ch)
        return

    if node not in graph:
        return

    for information in graph[node]:
        if full_path:
            needed_key = sum(full_path.keys())
            if counter + information[1] > needed_key:
                continue
        counter += information[1]
        current_distances.append(information[0])
        dfs(information[0], final_city, graph, full_paths, visited, counter, current_distances)
        current_distances.pop()
        counter -= information[1]


paths = int(input())
graph = {}

for _ in range(paths):
    start_point, end_point, distance = [int(ch) for ch in input().split(', ')]
    if start_point not in graph:
        graph[start_point] = []

    graph[start_point].append((end_point, distance))

starting_city = int(input())
final_city = int(input())
full_path = {}

dfs(starting_city, final_city, graph, full_path, set(), 0, [])
if not full_path:
    print("There is no such path.")
else:
    for key in dict(sorted(full_path.items(), key=lambda x: x)):
        print(key)
        full_path[key].insert(0, starting_city)
        print(*full_path[key], sep=' ')
        break
