from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = [-1] * N
ans[0] = 0
queue = deque([0])

while queue:
    next = queue.popleft()
    for node in G[next]:
        if ans[node] == -1:
            ans[node] = ans[next] + 1
            queue.append(node)

for i in ans:
    print(i)
