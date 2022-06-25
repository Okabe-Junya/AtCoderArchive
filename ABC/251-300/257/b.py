N, K, Q = map(int, input().split())
tmp = [False] * N
A = list(map(int, input().split()))
L = list(map(int, input().split()))

for i in range(K):
    tmp[A[i] - 1] = True

for i in range(Q):
    if A[L[i] - 1] == N:
        continue
    
    if not tmp[A[L[i] - 1]]:
        tmp[A[L[i] - 1]] = True
        tmp[A[L[i] - 1] - 1] = False
        A[L[i] - 1] += 1
    
    
for i in range(N):
    if tmp[i]:
        print(i + 1, end=" ")