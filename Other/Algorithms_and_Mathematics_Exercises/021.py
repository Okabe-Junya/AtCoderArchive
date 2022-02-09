def factorial(n):  # n > 0
    if n == 0:
        return 1
    return n * factorial(n - 1)


def cmb(n, r):  # n > 0, r <= n
    return factorial(n) // (factorial(n - r) * factorial(r))


n, r = map(int, input().split())
print(cmb(n, r))