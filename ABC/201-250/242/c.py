INF = 998244353
N = int(input())
dp = [[0] * 9 for _ in range(N)]
for i in range(9):
    dp[0][i] = 1
for i in range(1, N):
    for j in range(9):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j]
        elif j == 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1] + dp[i - 1][j]
        dp[i][j] %= INF
#print(dp)
print(sum(dp[N - 1]) % INF)