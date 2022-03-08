H, W = map(int, input().split())
maze = []
seen = [[False] * W for _ in range(H)]
for _ in range(H):
    tmp = list(input())
    maze.append(tmp)

# print(maze)
s = g = ()
for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            s = (i, j)
        elif maze[i][j] == 'g':
            g = (i, j)


def dfs(s, g, maze):
    print(s)
    seen[s[0]][s[1]] = True
    if s == g:
        return True
    if (s[0] > 0):
        if (maze[s[0] - 1][s[1]] == '.') & (not seen[s[0] - 1][s[1]]):  # up
            return dfs((s[0] - 1, s[1]), g, maze)
    if (s[0] < H - 1):
        if (maze[s[0] + 1][s[1]] == '.') & (not seen[s[0] + 1][s[1]]):  # down
            return dfs((s[0] + 1, s[1]), g, maze)
    if (s[1] > 0):
        if (maze[s[0]][s[1] - 1] == '.') & (not seen[s[0]][s[1] - 1]):  # left
            return dfs((s[0], s[1] - 1), g, maze)
    if (s[1] < W - 1):
        if (maze[s[0]][s[1] + 1] == '.') & (not seen[s[0]][s[1] + 1]):  # right
            return dfs((s[0], s[1] + 1), g, maze)
    return False


ans = dfs(s, g, maze)
print(ans)
