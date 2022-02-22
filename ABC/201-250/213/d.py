import sys

sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

for i in range(N):
    G[i] = sorted(G[i])

seen = [False] * N
ans = []
def dfs(v):
    ans.append(v)
    seen[v] = True
    for i in G[v]:
        if not seen[i]:
            dfs(i)
            ans.append(v)
    return

#print(G)
dfs(0)
#print(ans)
for i in ans:
    print(i + 1, end=' ')