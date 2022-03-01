import sys

INF = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 5)

def factorial(n):  # n > 0
    if n == 0:
        return 1
    return n * factorial(n - 1) % INF


N, M = map(int, input().split())
if abs(N - M) >= 2:
    print(0)
elif N == M:
    print(2 * factorial(N) * factorial(M) % INF)
else:
    print(factorial(N) * factorial(M) % INF)