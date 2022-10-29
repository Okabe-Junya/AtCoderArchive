INF = 998244353
N, M, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(K + 1)]
cnt = 0
dp[0][0] = 1
for i in range(K):
    for j in range(N + 1):
        if j == N:
            cnt += dp[i + 1][j]
            dp[i + 1][j] = 0
            cnt %= INF
        for k in range(1, M + 1):
            if j + k <= N:
                dp[i + 1][j + k] += dp[i][j]
                dp[i + 1][j + k] %= INF
            else:
                dp[i + 1][N - (j + k + 1)] += dp[i][j]
                dp[i + 1][N - (j + k + 1)] %= INF


def inv(a, m):  # a < m, mが素数
    def pos(x, n, m):
        if n == 0:
            return 1
        res = pos((x**2) % m, n // 2, m)
        if n % 2 == 1:
            res = res * x % m
        return res

    return pos(a, m - 2, m)


def pos(x, n, m):
    if n == 0:
        return 1
    res = pos((x**2) % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


cnt_all = pos(M, K, INF)
tmp = inv(cnt_all, INF)
print(cnt * tmp % INF)

