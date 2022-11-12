N, M = map(int, input().split())
A = list(map(int, input().split()))
if N == 1:
    print(0)
    exit()

Asum = sum(A)
Adic = {}

for i in range(N):
    if A[i] in Adic:
        Adic[A[i]] += 1
    else:
        Adic[A[i]] = 1

A = list(set(A))
A.sort()
cnt = []
tmp = 0

for i in range(len(A)):
    tmp += Adic[A[i]] * A[i]
    if (A[i] + 1) % M not in Adic:
        cnt.append(tmp)
        tmp = 0
if A[-1] == M - 1 and A[0] == 0:
    if not cnt:
        cnt.append(0)
    tmp += cnt[0]
cnt.append(tmp)
# print(cnt)

print(Asum - max(cnt))
