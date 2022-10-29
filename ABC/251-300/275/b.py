A, B, C, D, E, F = map(int, input().split())
INF = 998244353
a = (A * B * C) % INF
b = (D * E * F) % INF
print((a - b) % INF)
