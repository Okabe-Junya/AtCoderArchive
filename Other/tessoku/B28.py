N = int(input())
a1 = 1
a2 = 1
INF = 10**9 + 7
for i in range(N - 2):
    a1, a2 = a2, (a1 + a2) % INF

print(a2)
