N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

seen = [False] * N
stack = [0]
while stack:
    v = stack.pop()
    if seen[v]:
        continue
    seen[v] = True
    for u in G[v]:
        if not seen[u]:
            stack.append(u)

print("The graph is connected." if all(seen) else "The graph is not connected.")
