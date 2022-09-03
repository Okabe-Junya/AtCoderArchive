import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[-math.inf] * (N + 1) for _ in range(M + 1)]
dp[1] = [-math.inf] + A

for i in range(2, M + 1):
    tmp_max = -math.inf
    for j in range(1, N + 1):
        if tmp_max < dp[i - 1][j - 1]:
            tmp_max = dp[i - 1][j - 1]
        if i > j:
            continue
        dp[i][j] = tmp_max + (i * A[j - 1])


print(max(dp[-1]))
