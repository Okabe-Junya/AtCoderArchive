N, M = map(int, input().split())
G = [[] for _ in range(N)]
ans = 0
seen = [False] * N
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

for i in range(N):
    if seen[i]:
        continue
    ans += 1
    seen[i] = True
    stack = [i]
    while stack:
        v = stack.pop()
        for nv in G[v]:
            if seen[nv]:
                continue
            seen[nv] = True
            stack.append(nv)
print(ans)
