from collections import deque

H, W = map(int, input().split())
maze = []
seen = [[-1] * W for _ in range(H)]
seen[0][0] = 0
queue = deque([(0, 0)])
for i in range(H):
    maze.append(list(input()))

root = []

while queue:
    x, y = queue.popleft()
    if x == H - 1 and y == W - 1:
        break
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != '#' and seen[nx][ny] == -1:
            seen[nx][ny] = seen[x][y] + 1
            queue.append((nx, ny))

if seen[H - 1][W - 1] == -1:
    print(-1)
    exit()
else:
    tmp = (H - 1, W - 1)
    start = seen[H - 1][W - 1]
    while start > 0:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = tmp[0] + dx, tmp[1] + dy
            if 0 <= nx < H and 0 <= ny < W and seen[nx][ny] == start - 1:
                start = seen[nx][ny]
                tmp = (nx, ny)
                break
        root.append(tmp)

ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
            ans += 1
print(ans - len(root) - 1)