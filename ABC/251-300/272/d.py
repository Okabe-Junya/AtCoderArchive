from collections import deque


N, M = map(int, input().split())

ans = [[-1] * N for _ in range(N)]
ans[0][0] = 0
seen = [[False] * N for _ in range(N)]

d = []
for i in range(N):
    for j in range(N):
        if i ** 2 + j ** 2 == M:
            d.append((i, j))
            d.append((-i, j))
            d.append((i, -j))
            d.append((-i, -j))

queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    if seen[x][y]:
        continue
    seen[x][y] = True
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if not seen[nx][ny]:
                ans[nx][ny] = ans[x][y] + 1
                queue.append((nx, ny))

for i in range(N):
    for j in range(N):
        print(ans[i][j], end=' ')
    print()
