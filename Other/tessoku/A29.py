# xのn乗をmで割った余り
def pos(x, n, m):
    if n == 0:
        return 1
    res = pos((x**2) % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


a, b = map(int, input().split())
INF = 10**9 + 7
print(pos(a, b, INF))
