from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    
    visited_start = {start}
    queue_start = deque([start])
    parent_start = {start: None}

    
    visited_goal = {goal}
    queue_goal = deque([goal])
    parent_goal = {goal: None}

    while queue_start and queue_goal:
        
        if queue_start:
            current_start = queue_start.popleft()
            for neighbor in graph[current_start]:
                if neighbor not in visited_start:
                    visited_start.add(neighbor)
                    parent_start[neighbor] = current_start
                    queue_start.append(neighbor)

                    if neighbor in visited_goal:
                        return construct_path(parent_start, parent_goal, neighbor)

        
        if queue_goal:
            current_goal = queue_goal.popleft()
            for neighbor in graph[current_goal]:
                if neighbor not in visited_goal:
                    visited_goal.add(neighbor)
                    parent_goal[neighbor] = current_goal
                    queue_goal.append(neighbor)

                    if neighbor in visited_start:
                        return construct_path(parent_start, parent_goal, neighbor)

    return None  


def construct_path(parent_start, parent_goal, meeting_node):
    
    path_start = []
    node = meeting_node
    while node:
        path_start.append(node)
        node = parent_start[node]
    path_start.reverse()

    path_goal = []
    node = parent_goal[meeting_node]
    while node:
        path_goal.append(node)
        node = parent_goal[node]

    return path_start + path_goal


# -------- User Input --------
graph = {}
num_nodes = int(input("Enter number of nodes: "))
num_edges = int(input("Enter number of edges: "))

for _ in range(num_nodes):
    node = input("Enter node name: ")
    graph[node] = []

print("\nEnter edges (node1 node2):")
for _ in range(num_edges):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)  

start_node = input("\nEnter start node: ")
goal_node = input("Enter goal node: ")

path = bidirectional_search(graph, start_node, goal_node)

if path:
    print("\nPath found:")
    print(" -> ".join(path))
else:
    print("\nNo path found between", start_node, "and", goal_node)
