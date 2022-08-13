import sys

sys.setrecursionlimit(10**6)

N = int(input())
C = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

seen = [False] * N
color = {}
ans = []

def dfs(seen, color, v):
    seen[v] = True
    if C[v] in color:
        color[C[v]] += 1
    else:
        color[C[v]] = 1
    print(v, color)
    for u in G[v]:
        if not seen[u]:
            if (C[u] not in color) or (color[C[u]] == 0):
                ans.append(u)
            dfs(seen, color, u)
        color[C[u]] -= 1


dfs(seen, color, 0)
print(ans)
ans.sort()
for i in ans:
    print(i + 1)