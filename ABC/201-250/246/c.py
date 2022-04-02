N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
AX = []
Amod = []
ans = sum(A)
for i in range(N):
    AX.append(A[i] // X)
    Amod.append(A[i] % X)

Amod.sort(reverse=True)
for i in range(N):
    if K - AX[i] < 0:
        ans -= K * X
        print(ans)
        exit()
    K -= AX[i]
    ans -= AX[i] * X

if K > N:
    print(0)
    exit()
for i in range(K):
    ans -= Amod[i]
print(ans)