def a_star(graph, heuristic, start, goal):
    open_list = [(start, 0)]  
    parent = {start: None}
    g = {start: 0}

    while open_list:
        current = min(open_list, key=lambda x: g[x[0]] + heuristic[x[0]])
        open_list.remove(current)
        node = current[0]

        if node == goal:
            break

        for neighbor, cost in graph.get(node, []):
            new_g = g[node] + cost
            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                parent[neighbor] = node
                open_list.append((neighbor, new_g))

    path = []
    n = goal
    while n is not None:
        path.append(n)
        n = parent[n]
    path.reverse()
    return path,g[goal]

graph = {}
nodes = input("Enter all nodes (space separated): ").split()
m = int(input("Enter number of edges: "))

print("Enter edges (u v cost):")
for _ in range(m):
    u, v, w = input().split()
    w = float(w)
    if u not in graph: graph[u] = []
    if v not in graph: graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))

heuristic = {}
for node in nodes:
    heuristic[node] = float(input("h("+node+") = "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path, cost = a_star(graph, heuristic, start, goal)

print("\n===== RESULT =====")
print("Path:", " -> ".join(path))
print("Cost:", cost)
