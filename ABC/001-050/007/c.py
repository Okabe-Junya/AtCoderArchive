from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
sy -= 1; sx -= 1
gy, gx = map(int, input().split())
gy -= 1; gx -= 1
maze = []
seen = [[-1] * C for _ in range(R)]
seen[sy][sx] = 0
queue = deque([(sy, sx)])
for i in range(R):
    maze.append(list(input()))

while queue:
    y, x = queue.popleft()
    if y == gy and x == gx:
        # print(*seen)
        print(seen[y][x])
        exit()
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and maze[ny][nx] != '#' and seen[ny][nx] == -1:
            seen[ny][nx] = seen[y][x] + 1
            queue.append((ny, nx))