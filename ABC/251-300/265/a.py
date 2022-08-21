X, Y, N = map(int, input().split())
a = X * N
b = Y * (N // 3) + (N % 3) * X
print(min(a, b))
