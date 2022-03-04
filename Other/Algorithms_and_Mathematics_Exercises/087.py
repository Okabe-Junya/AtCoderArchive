INF = 10 ** 9 + 7
N = int(input())


def inv(a, m):  # a < m, mが素数
    def pos(x, n, m):
        if n == 0:
            return 1
        res = pos((x ** 2) % m, n // 2, m)
        if n % 2 == 1:
            res = res * x % m
        return res
    return pos(a, m - 2, m)


tmp = ((N ** 2) % INF) * (((N + 1) ** 2) % INF)
print((tmp * inv(4, INF)) % INF)