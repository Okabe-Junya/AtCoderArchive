n, m, t = map(int, input().split())
xy = [map(int, input().split()) for _ in range(m)]
x, y = [list(i) for i in zip(*xy)]
ns = n
a = 0
for k in range(m):
    n = n - (x[k] - a)
    if n <= 0:
        print('No')
        break
    if n + y[k] - x[k] <= ns:
        n = n + y[k] - x[k]
    else:
        n = ns
    a = y[k]
else:
    if n > t - y[m-1]:
        print('Yes')
    else:
        print('No')
