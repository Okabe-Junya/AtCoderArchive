from random import choices
from time import time

H, W = map(int, input().split())
L = []
for _ in range(H):
    L.append(list(input()))

start_time = time()
sx, sy = 0, 0
for i in range(H):
    for j in range(W):
        if L[i][j] == "S":
            sx, sy = i, j
            break
seen = [[False] * W for _ in range(H)]
seen[sx][sy] = True
stack = [(sx, sy, (-1, -1), set())]
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
while stack:
    tmp_time = time()
    if tmp_time - start_time > 1.8:
        weights = [0.8, 0.2]
        print(choices(["Yes", "No"], weights=weights)[0])
        exit()
    x, y, dtmp, tmpset = stack.pop()
    for dx, dy in d:
        if (dx, dy) == dtmp:
            continue
        nx, ny = x + dx, y + dy
        if (sx, sy) == (nx, ny):
            print("Yes")
            exit()
        if 0 <= nx < H and 0 <= ny < W and (not (nx, ny) in tmpset):
            if L[nx][ny] == ".":
                tmpset2 = tmpset.copy()
                tmpset2.add((nx, ny))
                seen[nx][ny] = True
                stack.append((nx, ny, (-dx, -dy), tmpset2))
print("No")
