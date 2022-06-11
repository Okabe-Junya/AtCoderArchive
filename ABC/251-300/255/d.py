from bisect import bisect_right

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
Asum = [A[0]]
for i in range(1, N):
    Asum.append(Asum[-1] + A[i])

for _ in range(Q):
    X = int(input())
    pr = bisect_right(A, X)
    if pr == 0:
        print(Asum[-1] - X * N)
        continue
    elif pr == N:
        print(X * N - Asum[-1])
        continue
    ans1 = abs(X * pr - Asum[pr - 1])
    ans2 = abs(Asum[-1] - Asum[pr - 1] - X * (N - pr))
    print(ans1 + ans2)