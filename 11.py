# Map adjacency
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

solution = {}

def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

def map_coloring():
    if len(solution) == len(graph):
        return True

    region = list(graph.keys())[len(solution)]

    for color in colors:
        if is_safe(region, color):
            solution[region] = color
            if map_coloring():
                return True
            del solution[region]

    return False


if map_coloring():
    print("Solution:")
    for region in solution:
        print(region + ":", solution[region])
else:
    print("No solution found")
