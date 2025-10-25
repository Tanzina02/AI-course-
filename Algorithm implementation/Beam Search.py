from queue import PriorityQueue

def beam_search(graph, start, goal, heuristic, beam_width):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))  
    parent = {start: None}

    while not frontier.empty():
        
        current_level = []
        while not frontier.empty():
            current_level.append(frontier.get())

        current_level = current_level[:beam_width]
        print(current_level)

        for i,current in current_level:
            if current == goal:
                path = []
                node = goal
                while node is not None:
                    path.append(node)
                    node = parent[node]
                path.reverse()
                return path

            for neighbor in graph.get(current, []):
                if neighbor not in parent: 
                    parent[neighbor] = current
                    frontier.put((heuristic[neighbor], neighbor))

    return None


graph = {}
nodes = input("Enter all nodes (separated by space): ").split()

for node in nodes:
    neighbors = input("Enter neighbors of " +node+" (separated by space, empty if none): ").split()
    graph[node] = neighbors

heuristic = {}
for node in nodes:
    h = int(input("Enter heuristic value h("+node+"): "))
    heuristic[node] = h

start = input("Enter start node: ")
goal = input("Enter goal node: ")
beam_width = int(input("Enter beam width (k): "))

path = beam_search(graph, start, goal, heuristic, beam_width)

print("\n===== RESULT =====")
if path:
    print("Final Path:", " -> ".join(path))
else:
    print("Goal not found")
