N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Asum = []
Bsum = []
Atmp = set()
Btmp = set()
Anum = 1
Bnum = 1
for i in range(N):
    if A[i] not in Atmp:
        Anum ^= (A[i] ** 4)
        Atmp.add(A[i])
    if B[i] not in Btmp:
        Bnum ^= (B[i] ** 4)
        Btmp.add(B[i])
    Asum.append(Anum)
    Bsum.append(Bnum)

Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    if Asum[x - 1] == Bsum[y - 1]:
        print("Yes")
    else:
        print("No")