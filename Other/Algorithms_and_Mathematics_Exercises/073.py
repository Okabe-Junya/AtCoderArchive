INF = 10 ** 9 + 7

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0


def pos(x, n, m):
    if n == 0:
        return 1
    res = pos((x ** 2) % m, n // 2, m)
    if n % 2 == 1:
        res = res * x % m
    return res


for i in range(N):
    ans += pos(2, i, INF) * A[i] % INF
print(ans % INF)
