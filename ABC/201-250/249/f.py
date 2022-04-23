N, K = map(int, input().split())
x = []
T = []
Y = []
tmpx = 0
for _ in range(N):
    t, y = map(int, input().split())
    T.append(t)
    Y.append(y)
    if t == 1:
        tmpx = y
        x.append(tmpx)
    else:
        tmpx += y
        x.append(tmpx)
diff = []
for i in range(N - 1):
    diff.append(x[i + 1] - x[i])
print(diff)