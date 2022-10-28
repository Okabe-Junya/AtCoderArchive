from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for _ in range(Q):
    print(bisect_left(A, int(input())))
