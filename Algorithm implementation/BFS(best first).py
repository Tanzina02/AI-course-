from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))  
    visited = set()
    parent = {start: None}
    
    while not frontier.empty():
        i,current = frontier.get()
        
        if current in visited:
            continue
        visited.add(current)
        
        print("Visiting:", current)
        
        if current == goal:

            path = []
            node = goal
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                parent[neighbor] = current
                frontier.put((heuristic[neighbor], neighbor))
    
    return None  

graph = {}
nodes = input("Enter all nodes (separated by space): ").split()

for node in nodes:
    neighbors = input("Enter neighbors of "+ node + " (separated by space, empty if none): ").split()
    graph[node] = neighbors

heuristic = {}
for node in nodes:
    h = int(input("Enter heuristic value h("+ node + "): "))
    heuristic[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")

path = best_first_search(graph, start, goal, heuristic)

print("\n===== RESULT =====")
if path:
    print("Final Path:", " -> ".join(path))
else:
    print("Goal note found")
