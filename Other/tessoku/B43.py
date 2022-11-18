N, M = map(int, input().split())
A = list(map(int, input().split()))
dict = {}
for i in range(M):
    if A[i] in dict:
        dict[A[i]] += 1
    else:
        dict[A[i]] = 1

for i in range(N):
    if i + 1 in dict:
        print(M - dict[i + 1])
    else:
        print(M)
