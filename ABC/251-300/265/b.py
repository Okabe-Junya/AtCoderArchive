N, M, T = map(int, input().split())
A = list(map(int, input().split()))
L = {}
for _ in range(M):
    X, Y = map(int, input().split())
    L[X] = Y


i = 0
while i < N - 1:
    T -= A[i]
    if T <= 0:
        print('No')
        exit()
    if i + 2 in L:
        T += L[i + 2]
    i += 1
print('Yes')
