def cmb_mod(n: int, r: int, INF=10**9 + 7) -> int:
    """nCr mod INF, INF: prime number"""

    def pos(x, n, m):
        if n == 0:
            return 1
        res = pos((x**2) % m, n // 2, m)
        if n % 2 == 1:
            res = res * x % m
        return res

    def fact(n: int) -> int:
        retval = 1
        for i in range(1, n + 1):
            retval *= i
            retval %= INF
        return retval

    if (r < 0) or (n < r):
        return 0

    a = fact(n)
    b = fact(r) * fact(n - r) % INF
    return a * pos(b, INF - 2, INF) % INF


# 階乗
def factorial(n):  # n > 0
    if n == 0:
        return 1
    return n * factorial(n - 1)


X, Y = map(int, input().split())
INF = 998244353
print(
    (
        factorial(X + Y)
        - factorial(X + Y - 2) * cmb_mod(X, 3, INF) * cmb_mod(Y, 3, INF) * 6
    )
    % INF
)
