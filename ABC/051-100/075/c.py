N, M = map(int, input().split())
G_in = []
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    G_in.append([a - 1, b - 1])

def dfs(G, v, seen):
    seen[v] = True
    for i in G[v]:
        if not seen[i]:
            dfs(G, i, seen)


for i in range(M):
    G = [[] for _ in range(N)]
    seen = [False] * N
    for j in range(M):
        if i != j:
            G[G_in[j][0]].append(G_in[j][1])
            G[G_in[j][1]].append(G_in[j][0])
    dfs(G, 0, seen)
    for node in seen:
        if not node:
            ans += 1
            break

print(ans)