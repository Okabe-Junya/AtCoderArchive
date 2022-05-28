N, M, K = map(int, input().split())
INF = 998244353
dp = [[0] * M for _ in range(N)]
dpsum = [[0] * M for _ in range(N)]
dpsum[0][0] = 1
for i in range(M):
    dp[0][i] = 1

for i in range(1, M):
    dpsum[0][i] = dpsum[0][i - 1] + dp[0][i]

for i in range(1, N):
    for j in range(M):
        if j - K >= 0:
            dp[i][j] += dpsum[i - 1][j - K]
        if j + K < M:
            dp[i][j] += dpsum[i - 1][-1] -  dpsum[i - 1][j + K - 1]
        elif (j - K) < 0 and (j + K) >= M:
            dp[i][j] = 0
        dp[i][j] %= INF
        if j == 0:
            dpsum[i][j] = dp[i][j]
        else:
            dpsum[i][j] = dpsum[i][j - 1] + dp[i][j]
print(sum(dp[-1]) % INF)