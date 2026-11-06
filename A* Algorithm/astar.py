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
}import heapq

def a_star_search(start, goal):
    # Priority queue stores tuples of (f_score, current_node, path, g_score)
    pq = []
    heapq.heappush(pq, (heuristics[start], start, [start], 0))
    visited = set()
    
    while pq:
        f, current, path, g = heapq.heappop(pq)
        
        if current == goal:
            return path, g
            
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                g_score = g + cost
                f_score = g_score + heuristics.get(neighbor, 0)
                heapq.heappush(pq, (f_score, neighbor, path + [neighbor], g_score))
                
    return None, float('inf')

a_star_path, total_cost = a_star_search('A', 'G')
print(f"A* Path: {a_star_path} with Cost: {total_cost}")
