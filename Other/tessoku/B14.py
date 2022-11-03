N, K = map(int, input().split())
A = list(map(int, input().split()))
if N == 1:
    if K == A[0]:
        print("Yes")
    else:
        print("No")
    exit()
A1 = []
A2 = []
for i in range(N // 2):
    A1.append(A[i])
for i in range(N // 2, N):
    A2.append(A[i])

A1set = set()
A2set = set()
for i in range(2 ** len(A1)):
    sum = 0
    for j in range(len(A1)):
        if (i >> j) & 1:
            sum += A1[j]
    A1set.add(sum)
for i in range(2 ** len(A2)):
    sum = 0
    for j in range(len(A2)):
        if (i >> j) & 1:
            sum += A2[j]
    A2set.add(sum)

for num in A1set:
    if K - num in A2set:
        print("Yes")
        exit()
print("No")
