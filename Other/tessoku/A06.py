N, Q = map(int, input().split())
A = list(map(int, input().split()))
Asum = [0]
for i in range(N):
    Asum.append(Asum[-1] + A[i])
for _ in range(Q):
    L, R = map(int, input().split())
    print(Asum[R] - Asum[L - 1])
