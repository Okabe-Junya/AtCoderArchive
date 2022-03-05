n = int(input())
x = list(map(int, input().split()))
y = sorted(x)
xl = y[n // 2 - 1]
xr = y[n // 2]
for i in range(n):
    if x[i] >= xr:
        print(xl)
    else:
        print(xr)
