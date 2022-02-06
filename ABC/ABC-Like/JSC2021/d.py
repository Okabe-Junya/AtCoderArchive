def pos(x, n, m):
    if n == 0:
        return 1
    res = pos(x*x % m, n//2, m)
    if n % 2 == 1:
        res = res*x % m
    return res


n, p = map(int, input().split())
INF = 10 ** 9 + 7
if n == 1:
    print(p-1)
else:
    ans = (p-1) * pos(p-2, n-1, INF)
    print(ans % INF)
