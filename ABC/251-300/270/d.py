from bisect import bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
ans = 0
while N != 0:
    p = bisect_right(A, N)
    # print("N:", N)
    if cnt % 2 == 0:
        ans += A[p - 1]
        # print("A[p - 1]:", A[p - 1])
    N -= A[p - 1]
    cnt += 1

# print(N)
print(ans)
