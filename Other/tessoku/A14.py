N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = set()
CD = set()

for i in range(N):
    for j in range(N):
        AB.add(A[i] + B[j])
        CD.add(C[i] + D[j])

for x in AB:
    if K - x in CD:
        print('Yes')
        exit()
print('No')
