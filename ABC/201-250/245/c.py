N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [[False] * 2 for _ in range(N)]
dp[0][0] = True
dp[0][1] = True
for i in range(1, N):
    if (dp[i - 1][0]) & (abs(A[i] - A[i - 1]) <= K):
        dp[i][0] = True
    if (dp[i - 1][1]) & (abs(A[i] - B[i - 1]) <= K):
        dp[i][0] = True
    if (dp[i - 1][0]) & (abs(B[i] - A[i - 1]) <= K):
        dp[i][1] = True
    if (dp[i - 1][1]) & (abs(B[i] - B[i - 1]) <= K):
        dp[i][1] = True
if dp[N - 1][0] or dp[N - 1][1]:
    print("Yes")
else:
    print("No")
