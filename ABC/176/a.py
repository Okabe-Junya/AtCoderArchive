n, x, t = map(int, input().split())
if n % x == 0:
    a = 0
else:
    a = t
print(n // x * t + a)
