def cmb(n, r):  # n > 0, r <= n
    def factorial(n):  # n > 0
        if n == 0:
            return 1
        return n * factorial(n - 1)

    return factorial(n) // (factorial(n - r) * factorial(r))


N = int(input())
INF = 998244353
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

ans = [0] * N
for i in range(1, N + 1):  # 頂点をiこ選ぶ
    for j in range(i):  # 頂点をjこ選ぶ
        ans[j] += cmb(N - j, i - j)
print(*ans, sep="\n")
