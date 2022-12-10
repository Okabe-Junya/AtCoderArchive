N, K, D = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
AD = []
for i in range(N):
    AD.append(A[i] % D)


# 部分和問題（DP）
def subset_sum(num_list: list[int], S: int):
    N = len(num_list)
    dp = [[(False, 0) for _ in range(S + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = (True, 0)

    for i in range(1, N + 1):
        for j in range(1, S + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= num_list[i - 1]:
                if dp[i - 1][j - num_list[i - 1]][0]:
                    dp[i][j] = (True, dp[i - 1][j - num_list[i - 1]][1] + 1)
    return dp


print(subset_sum(AD, 4))
