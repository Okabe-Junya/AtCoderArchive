S = input()
T = input()

dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]

for i in range(len(S) + 1):
    for j in range(len(T) + 1):
        if i == 0 or j == 0:
            continue
        if S[i - 1] == T[j - 1]:
            dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
