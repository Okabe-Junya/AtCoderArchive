N, W = map(int, input().split())
l = []
for _ in range(N):
    w, v = map(int, input().split())
    l.append((w, v))
    
dp = [[0] * (W + 1) for _ in range(N)] # dp[i][j] : i-1番目までの荷物で重さj以下になるような最大価値
for i in range(N):
    for j in range(W + 1):
        if j - l[i][0] >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - l[i][0]] + l[i][1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])