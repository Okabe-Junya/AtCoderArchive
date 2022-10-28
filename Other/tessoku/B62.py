N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

seen = [False] * N
prev = [-1] * N
seen[0] = True
stack = [0]
while stack:
    v = stack.pop()
    for u in G[v]:
        if not seen[u]:
            seen[u] = True
            prev[u] = v
            stack.append(u)
ans = []
start = N - 1
while prev[start] != -1:
    ans.append(start)
    start = prev[start]
ans.append(0)
for i in range(len(ans) - 1, -1, -1):
    print(ans[i] + 1, end=' ')
print()
