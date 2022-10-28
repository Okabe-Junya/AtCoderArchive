N, W = map(int, input().split())
L = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W + 1) for _ in range(N)]
for i in range(N):
    w, v = L[i]
    for j in range(W + 1):
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
print(dp[-1][-1])
