import sys

sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    G[u - 1].append((v - 1, w))
    G[v - 1].append((u - 1, w))

ans = [-1] * N
ans[0] = 0


def dfs(u):
    for v, w in G[u]:
        if ans[v] == -1:
            if w % 2 == 0:
                ans[v] = ans[u]
            else:
                ans[v] = 1 - ans[u]
            dfs(v)


dfs(0)
for i in ans:
    print(i)
