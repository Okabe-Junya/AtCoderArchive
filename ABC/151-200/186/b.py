h, w = map(int, input().split())
a = [input().split() for l in range(h)]
min = int(a[0][0])
cnt = 0
for i in range(h):
    for j in range(w):
        a[i][j] = int(a[i][j])
        if a[i][j] < min:
            min = a[i][j]
for i in range(h):
    for j in range(w):
        if a[i][j] != min:
            cnt += a[i][j] - min
print(cnt)
