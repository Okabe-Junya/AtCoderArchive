N, K = map(int, input().split())
INF = 10 ** 9 + 7


def pos(x, n, m):
    if n == 0:
        return 1
    res = pos(x * x % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


if K == 1:
    if N == 1:
        print(1)
    else:
        print(0)
    exit()
if N == 1:
    print(K)
    exit()

tmp = (K * (K - 1)) % INF
tmp *= pos(K - 2, N - 2, INF)
ans = tmp % INF

print(ans)
