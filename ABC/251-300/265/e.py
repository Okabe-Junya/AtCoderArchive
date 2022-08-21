N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
L = set()
for _ in range(M):
    X, Y = map(int, input().split())
    L.add((X, Y))
INF = 998244353

dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(N + 1 - i):
        for k in range(N + 1 - i - j):
            if i == 0 and j == 0 and k == 0:
                dp[i][j][k] = 1
                continue
            dp[i][j][k] = dp[i - 1][j][k] + dp[i][j - 1][k] + dp[i][j][k - 1]
            if (A * i + C * j + E * k, B * i + D * j + F * k) in L:
                dp[i][j][k] = 0
            dp[i][j][k] %= INF

ans = 0
for i in range(N + 1):
    for j in range(N + 1):
        ans += dp[i][j][N - i - j]
        ans %= INF
print(ans)
