N, M, K = map(int, input().split())
INF = 998244353
ans = 0
dp = [[0] * K for _ in range(N)] # n項までで和がk-1
for i in range(min(M, K)):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(i, K):
        for k in range(1, M + 1):
            if j - k >= 0:
                dp[i][j] += dp[i - 1][j - k]
                dp[i][j] %= INF
        dp[i][j] %= INF
#print(dp)
print(sum(dp[N - 1]) % INF)