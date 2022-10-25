INF = 10**9 + 7

N, P = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] %= INF

Adict = {}
for a in A:
    if a in Adict:
        Adict[a] += 1
    else:
        Adict[a] = 1

if P == 0:
    if 0 not in Adict:
        print(0)
    else:
        print(Adict[0] * (Adict[0] - 1) // 2 + Adict[0] * (N - Adict[0]))
    exit()


# フェルマーの小定理を用いた逆元計算（法mが素数である必要がある）
def inv(a, m):  # a < m, mが素数
    def pos(x, n, m):
        if n == 0:
            return 1
        res = pos((x**2) % m, n // 2, m)
        if n % 2 == 1:
            res = res * x % m
        return res

    return pos(a, m - 2, m)


ans = 0
for i in A:
    Adict[i] = max(0, Adict[i] - 1)
    tmp = inv(i, INF) * P % INF
    if tmp in Adict:
        ans += Adict[tmp]
print(ans)
