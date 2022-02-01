h, w, x, y = map(int, input().split())
s = [list(input()) for i in range(h)]
ans = -3
for i in range(y-1, w):
    if s[x-1][i] == '#':
        break
    ans += 1
for i in range(y):
    if s[x-1][y-1-i] == '#':
        break
    ans += 1
for i in range(x-1, h):
    if s[i][y-1] == '#':
        break
    ans += 1
for i in range(x):
    if s[x-1-i][y-1] == '#':
        break
    ans += 1
print(ans)
