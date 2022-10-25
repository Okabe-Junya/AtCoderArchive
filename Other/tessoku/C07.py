from bisect import bisect_right

N = int(input())
C = list(map(int, input().split()))
C.sort()
Csum = [C[0]]
for i in range(1, N):
    Csum.append(Csum[i - 1] + C[i])

Q = int(input())
for _ in range(Q):
    X = int(input())
    print(bisect_right(Csum, X))
