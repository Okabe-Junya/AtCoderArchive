INF = 10 ** 9 + 7
n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [INF] * (n + 1)
dp[1] = 0
for i in range(1, n + 1): # 足場iまでの最小コスト
    for j in range(1, k + 1):
        if i - j < 0:
            continue
        dp[i] = min(dp[i], dp[i - j] + abs(h[i - 1] - h[i - j - 1]))
print(dp[-1])
    