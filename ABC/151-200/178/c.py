INF = 10 ** 9 + 7


def pos(x, n, m):
    if n == 0:
        return 1
    res = pos((x ** 2) % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


N = int(input())
if N == 1:
    print(0)
    exit()

a = pos(10, N, INF) - 2 * pos(9, N, INF)
b = pos(8, N, INF)
print((a + b) % INF)