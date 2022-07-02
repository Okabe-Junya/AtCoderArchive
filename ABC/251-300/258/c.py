N, Q = map(int, input().split())
S = input()
p = 0
for _ in range(Q):
    n, x = map(int, input().split())
    if n == 1:
        p += x
    else:
        print(S[(x - p - 1) % N])