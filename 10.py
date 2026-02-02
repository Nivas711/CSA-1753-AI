import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    
    f_cost = {node: float('inf') for node in graph}
    f_cost[start] = heuristic[start]

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]

        for neighbor, cost in graph[current]:
            temp_g = g_cost[current] + cost

            if temp_g < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = temp_g
                f_cost[neighbor] = temp_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))

    return None, float('inf')


# Graph (no G node)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 6)],
    'C': [('F', 2)],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic values (estimate to reach F)
heuristic = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 6,
    'E': 6,
    'F': 0
}

path, cost = a_star(graph, 'A', 'F', heuristic)

print("Path:", path)
print("Cost:", cost)
