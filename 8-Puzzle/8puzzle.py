import heapq
import copy

# --- EDIT YOUR INPUT HERE ---
start = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
# ----------------------------

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.blank_pos = next((i, j) for i in range(3) for j in range(3) if board[i][j] == 0)

    def __lt__(self, other):
        return self.cost < other.cost

    def get_neighbors(self):
        neighbors = []
        r, c = self.blank_pos
        moves = {"Up": (r-1, c), "Down": (r+1, c), "Left": (r, c-1), "Right": (r, c+1)}
        for name, (nr, nc) in moves.items():
            if 0 <= nr < 3 and 0 <= nc < 3:
                nb = copy.deepcopy(self.board)
                nb[r][c], nb[nr][nc] = nb[nr][nc], nb[r][c]
                neighbors.append(PuzzleState(nb, self, name, self.depth + 1))
        return neighbors

def solve_puzzle(start_board, goal_board, heuristic_func):
    open_list = [PuzzleState(start_board)]
    open_list[0].cost = heuristic_func(start_board, goal_board)
    closed_set = set()
    nodes = 0

    while open_list:
        curr = heapq.heappop(open_list)
        nodes += 1
        if curr.board == goal_board:
            path = []
            while curr.parent:
                path.append((curr.move, curr.board))
                curr = curr.parent
            return path[::-1], nodes
        closed_set.add(tuple(tuple(r) for r in curr.board))
        for n in curr.get_neighbors():
            if tuple(tuple(r) for r in n.board) not in closed_set:
                n.cost = n.depth + heuristic_func(n.board, goal_board)
                heapq.heappush(open_list, n)
    return None, nodes

# Misplaced Tiles Heuristic
def misplaced_tiles(board, goal):
    return sum(1 for i in range(3) for j in range(3) if board[i][j] != 0 and board[i][j] != goal[i][j])

path, nodes = solve_puzzle(start, goal, misplaced_tiles)
print(f"--- SOLVED WITH MISPLACED TILES ---\nNodes Expanded: {nodes}\nSteps: {len(path)}")
for step, (move, board) in enumerate(path, 1):
    print(f"Step {step} ({move}): {board[0]} {board[1]} {board[2]}")
