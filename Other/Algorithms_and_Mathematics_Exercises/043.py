import sys


sys.setrecursionlimit(100000)
n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)
# print(edge)

can = [False] * n


def dfs(i):
    can[i] = True
    for i in edge[i]:
        if not can[i]:
            dfs(i)


dfs(0)
# print(can)
if sum(can) == n:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
