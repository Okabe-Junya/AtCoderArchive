N, M, E = map(int, input().split())
G = [set() for _ in range(N + M)]
L = []
for _ in range(E):
    a, b = map(int, input().split())
    L.append((a, b))
    G[a - 1].add(b - 1)
    G[b - 1].add(a - 1)

seen = [False] * (N + M)
for start in range(N, N + M):
    stack = [start]
    while stack:
        v = stack.pop()
        if seen[v]:
            continue
        seen[v] = True
        for u in G[v]:
            stack.append(u)
ans = sum(seen[:N])

Q = int(input())
for _ in range(Q):
    X = int(input())
    a, b = L[X - 1]
    G[a - 1].discard(b - 1)
    G[b - 1].discard(a - 1)
    print(G)
