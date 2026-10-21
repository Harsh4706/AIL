import heapq

def heuristic(state, n):
    d = 0
    for i, x in enumerate(state):
        if x != 0:
            goal = x - 1
            d += abs(i // n - goal // n) + abs(i % n - goal % n)
    return d

def astar(start, n):
    goal = tuple(range(1, n*n)) + (0,)
    pq = [(heuristic(start, n), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        z = state.index(0)
        r, c = z // n, z % n

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n:
                nz = nr * n + nc
                s = list(state)
                s[z], s[nz] = s[nz], s[z]
                s = tuple(s)

                if s not in visited:
                    heapq.heappush(pq, (g + 1 + heuristic(s, n),
                                        g + 1, s, path + [state]))
    return None

# Main
n = int(input("Enter N: "))
start = []

print("Enter puzzle row by row (0 for blank):")
for i in range(n):
    start += list(map(int, input().split()))

start = tuple(start)
solution = astar(start, n)

if solution:
    print("Solution found in", len(solution)-1, "moves")
    for state in solution:
        for i in range(0, n*n, n):
            print(state[i:i+n])
        print()
else:
    print("No solution found")