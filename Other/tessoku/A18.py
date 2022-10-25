# 部分和問題（DP）
def subset_sum(l: list, S: int) -> bool:  # list lのいくつかの合計をSにできるか
    N = len(l)
    dp = [[False for _ in range(S + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = True

    for i in range(1, N + 1):
        for j in range(1, S + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= l[i - 1]:
                dp[i][j] |= dp[i - 1][j - l[i - 1]]
    return dp[N][S]


N, S = map(int, input().split())
A = list(map(int, input().split()))
print("Yes" if subset_sum(A, S) else "No")
