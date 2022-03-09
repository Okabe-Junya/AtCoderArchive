INF = 10 ** 9 + 7


def pos(x, n, m):
    if n == 0:
        return 1
    res = pos((x ** 2) % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


K = int(input())
if K % 9 != 0:
    print(0)
else:
    print(pos(2, (K - 1), INF))