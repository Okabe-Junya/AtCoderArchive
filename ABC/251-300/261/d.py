N, M = map(int, input().split())
X = list(map(int, input().split()))
bonus = {}
for i in range(M):
    C, Y = map(int, input().split())
    bonus[C] = Y

dp = [[0] * (N + 1) for _ in range(N + 1)] # dp[i][j]: cntがjのとき，i番目までの最大値
prev_max = 0
tmp_max = 0
for i in range(N + 1):
    prev_max = tmp_max
    tmp_max = 0
    for j in range(N + 1):
        if j == 0:
            dp[i][j] = prev_max
        else:
            if j <= i:
                dp[i][j] = dp[i - 1][j - 1] + X[i - 1]
                if j in bonus:
                    dp[i][j] += bonus[j]
        if dp[i][j] > tmp_max:
            tmp_max = dp[i][j]
print(max(dp[N]))