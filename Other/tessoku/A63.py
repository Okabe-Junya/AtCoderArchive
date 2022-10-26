from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
seen = [-1] * N
seen[0] = 0
queue = deque([0])
while queue:
    v = queue.popleft()
    for u in G[v]:
        if seen[u] != -1:
            continue
        seen[u] = seen[v] + 1
        queue.append(u)

print(*seen, sep='\n')
