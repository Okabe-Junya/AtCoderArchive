import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
#print(G)
def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    for i in G[v]:
        dfs(i)
ans = 0
for i in range(n):     
    visited = [False] * (n + 1)
    dfs(i + 1)
    ans += sum(visited)
print(ans)