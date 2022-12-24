N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    L = list(map(int, input().split()))
    if L[0] == 1:
        A[L[1] - 1] = L[2]
    else:
        print(A[L[1] - 1])
