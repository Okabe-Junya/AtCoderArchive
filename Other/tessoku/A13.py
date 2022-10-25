from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N):
    p = bisect_right(A, A[i] + K)
    ans += p - i - 1
print(ans)
