import sys
sys.setrecursionlimit(10 ** 5)

x, y = map(int, input().split())
if x > y:
    x, y = y, x
INF = 10 ** 9 + 7


def cmb_mod(n, k, p):
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)
    
    def permutation(n, r):
        return factorial(n) // factorial(n - r)
    
    def inv(a, m):
        def pos(x, n, m):
            if n == 0:
                return 1
            res = pos((x ** 2) % m, n // 2, m)
            if n % 2 == 1:
                res = res * x % m
            return res
        return pos(a, m - 2, m)

    fact_k = factorial(k)
    invk = inv(fact_k, p)
    return (permutation(n, k) % p) * invk % p

print(cmb_mod(x + y, x, INF))