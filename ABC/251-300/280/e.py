from math import gcd


# フェルマーの小定理を用いた逆元計算（法mが素数である必要がある）
def inv(a, m=998244353):  # a < m, mが素数
    def pos(x, n, m):
        if n == 0:
            return 1
        res = pos((x**2) % m, n // 2, m)
        if n % 2 == 1:
            res = res * x % m
        return res

    return pos(a, m - 2, m)


N, P = map(int, input().split())
P1 = 100 - P
g = gcd(P, 100)
g1 = gcd(P1, 100)
invp = inv(100 // g) * (P // g) % 998244353
invp1 = inv(100 // g1) * (P1 // g1) % 998244353


dp = [-1] * (N + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = (invp1 * (dp[i - 1] + 1)) + (invp * (dp[i - 2] + 1))
    dp[i] %= 998244353
print(dp[-1])
