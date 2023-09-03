from collections import deque

N = int(input())
C = input()
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# 木構造の任意の2点間の距離を求める
dist = [[-1] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0

for i in range(N):
    q = deque()
    q.append(i)
    while q:
        v = q.popleft()
        for nv in G[v]:
            if dist[i][nv] == -1:
                dist[i][nv] = dist[i][v] + 1
                q.append(nv)

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if C[i] != C[j] and C[j] != C[k] and C[k] != C[i]:
                if dist[i][j] == dist[j][k] == dist[k][i]:
                    ans += 1
print(ans)
