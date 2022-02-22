n, x = map(int, input().split())
a = []
b = []
for _ in range(n):
    a1, b1 = map(int, input().split())
    a.append(a1)
    b.append(b1)

dp = [[False] * (x + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(1, n + 1):
    for j in range(x):
        if dp[i - 1][j]:
            if j + a[i - 1] <= x:
                dp[i][j + a[i - 1]] = True
            if j + b[i - 1] <= x:
                dp[i][j + b[i - 1]] = True

if dp[-1][-1]:
    print("Yes")
else:
    print("No")