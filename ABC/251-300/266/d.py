N = int(input())

dict = {}
for _ in range(N):
    T, X, A = map(int, input().split())
    dict[(T, X)] = A

dp = [[0] * 5 for _ in range(T + 1)]
for i in range(1, T + 1):
    for j in range(5):
        if i < j:
            continue
        if j == 0:
            dp[i][j] = max(dp[i - 1][0], dp[i - 1][1])
        elif 1 <= j <= 3:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
        else:
            dp[i][j] = max(dp[i - 1][3], dp[i - 1][4])
        if (i, j) in dict:
            dp[i][j] += dict[(i, j)]

print(max(dp[-1]))
