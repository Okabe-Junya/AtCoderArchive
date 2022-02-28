from scipy.special import comb as cmb


# xのn乗をmで割った余り
def pos(x, n, m):
    if n == 0:
        return 1
    res = pos((x ** 2) % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


INF = 10 ** 9 + 7
n, a, b = map(int, input().split())
ans = (pos(2, n, INF) - (cmb(n, a, exact=True) % INF) - (cmb(n, b, exact=True) % INF) - 1) % INF
print(ans)
