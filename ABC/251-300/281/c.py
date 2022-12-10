from bisect import bisect_left

N, T = map(int, input().split())
A = list(map(int, input().split()))
Asum = [A[0]]
for i in range(1, N):
    Asum.append(Asum[-1] + A[i])

T %= Asum[-1]
idx = bisect_left(Asum, T)
print(idx + 1, T - Asum[idx - 1] if idx > 0 else T)
