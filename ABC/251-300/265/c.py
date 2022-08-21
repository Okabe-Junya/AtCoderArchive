H, W = map(int, input().split())
G = []
for _ in range(H):
    G.append(list(input()))

seen = [[False] * W for _ in range(H)]
tmp = [0, 0]

while True:
    if seen[tmp[0]][tmp[1]]:
        print(-1)
        exit()
    seen[tmp[0]][tmp[1]] = True
    if G[tmp[0]][tmp[1]] == 'L':
        if tmp[1] == 0:
            print(tmp[0] + 1, tmp[1] + 1)
            exit()
        else:
            tmp[1] -= 1
    elif G[tmp[0]][tmp[1]] == 'R':
        if tmp[1] == W - 1:
            print(tmp[0] + 1, tmp[1] + 1)
            exit()
        else:
            tmp[1] += 1
    elif G[tmp[0]][tmp[1]] == 'U':
        if tmp[0] == 0:
            print(tmp[0] + 1, tmp[1] + 1)
            exit()
        else:
            tmp[0] -= 1
    elif G[tmp[0]][tmp[1]] == 'D':
        if tmp[0] == H - 1:
            print(tmp[0] + 1, tmp[1] + 1)
            exit()
        else:
            tmp[0] += 1
