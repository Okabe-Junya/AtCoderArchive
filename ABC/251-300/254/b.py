# 階乗
def factorial(n):  # n > 0
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 組み合わせ
def cmb(n, r):  # n > 0, r <= n
    def factorial(n):  # n > 0
        if n == 0:
            return 1
        return n * factorial(n - 1)
    return factorial(n) // (factorial(n - r) * factorial(r))

N = int(input())
for i in range(N):
    for j in range(i + 1):
        print(cmb(i, j), end=' ')
    print()