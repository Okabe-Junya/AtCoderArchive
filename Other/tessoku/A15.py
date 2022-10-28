from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))

Alist = sorted(list(set(A)))
ans = [0] * N
for i in range(N):
    ans[i] = bisect_right(Alist, A[i])

print(*ans)
