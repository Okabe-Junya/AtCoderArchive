N, K = map(int, input().split())
a = list(map(int, input().split()))

asort = sorted(a)
A = [[] for _ in range(K)]
for i in range(N):
    A[i % K].append(a[i])

for i in range(K):
    A[i] = sorted(A[i])

newA = []
for i in range(N):
    newA.append(A[i % K][i // K])

if newA == asort:
    print('Yes')
else:
    print('No')