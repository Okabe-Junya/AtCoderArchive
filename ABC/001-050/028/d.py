n, k = map(int, input().split())
a = (k - 1) * (n - k) * 6 + 3 * n - 2
b = n ** 3
print(a / b)
