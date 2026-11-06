graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 6)],
    'G': []
}

# Heuristic estimates to goal 'G'
heuristics = {
    'A': 6,
    'B': 3,
    'C': 5,
    'D': 4,
    'E': 1,
    'F': 5,
    'G': 0
}
def depth_limited_search(node, goal, depth, path):
    if depth == 0 and node == goal:
        return path
    if depth > 0:
        for neighbor, _ in graph.get(node, []):
            if neighbor not in path:
                result = depth_limited_search(neighbor, goal, depth - 1, path + [neighbor])
                if result is not None:
                    return result
    return None

def iterative_deepening_search(start, goal, max_depth=10):
    for depth in range(max_depth):
        print(f"Searching with depth limit: {depth}")
        path = depth_limited_search(start, goal, depth, [start])
        if path is not None:
            return path
    return None

ids_path = iterative_deepening_search('A', 'G')
print(f"IDS Path: {ids_path}")
