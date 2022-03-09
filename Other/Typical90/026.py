import sys

sys.setrecursionlimit(10 ** 5 + 1)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

color = [-1] * N

def dfs(tmp, c):
    color[tmp] = c
    for i in G[tmp]:
        if color[i] == -1:
            dfs(i, 1 - c)
            
dfs(0, 0)
cnt0 = 0
for i in range(N):
    if color[i] == 0:
        cnt0 += 1
if cnt0 >= N // 2:
    idx = 0
    for i in range(N):
        if color[i] == 0:
            if idx == N // 2:
                break
            print(i + 1, end=' ')
            idx += 1
else:
    idx = 0
    for i in range(N):
        if color[i] == 1:
            if idx == N // 2:
                break
            print(i + 1, end=' ')
            idx += 1
