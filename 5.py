from collections import deque

# Check if a state is valid
def is_valid(M_left, C_left):
    M_right = 3 - M_left
    C_right = 3 - C_left
    
    if M_left < 0 or C_left < 0 or M_left > 3 or C_left > 3:
        return False
    if (M_left > 0 and C_left > M_left):
        return False
    if (M_right > 0 and C_right > M_right):
        return False
    return True

# BFS to find solution
def solve():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (M_left, C_left, boat), path = queue.popleft()
        
        if (M_left, C_left, boat) == goal:
            return path + [(M_left, C_left, boat)]
        
        if (M_left, C_left, boat) in visited:
            continue
        visited.add((M_left, C_left, boat))
        
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        
        for m, c in moves:
            if boat == 0:  # boat on left → going right
                new_state = (M_left - m, C_left - c, 1)
            else:          # boat on right → going left
                new_state = (M_left + m, C_left + c, 0)
            
            if is_valid(new_state[0], new_state[1]):
                queue.append((new_state, path + [(M_left, C_left, boat)]))

solution = solve()

for step in solution:
    print(step)
