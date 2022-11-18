N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * (N)
for i in range(N - 1):
    dp[B[i] - 1] = max(dp[i] + 150, dp[B[i] - 1])
    dp[A[i] - 1] = max(dp[i] + 100, dp[A[i] - 1])
print(dp[-1])
