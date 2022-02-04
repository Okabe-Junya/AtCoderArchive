N, L = map(int, input().split())
INF = 10 ** 9 + 7

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    if (i - L) >= 0:
        dp[i] = dp[i - 1] + dp[i - L]
    else:
        dp[i] = dp[i - 1]
        
print(dp[-1] % INF)