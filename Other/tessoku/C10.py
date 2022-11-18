def pos(x, n, m):
    if n == 0:
        return 1
    res = pos((x**2) % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


W = int(input())
print(12 * pos(7, W - 1, 10**9 + 7) % (10**9 + 7))
