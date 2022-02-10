n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(2)] # dp[0][i]: i日目に勉強しない最大値
for i in range(1, n + 1):
    dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
    dp[1][i] = max(dp[0][i - 1] + a[i - 1], dp[1][i - 1])
    
print(dp[-1][-1])