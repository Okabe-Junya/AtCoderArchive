N, M = map(int, input().split())
A = []
for _ in range(M):
    C = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    A.append(a)

cnt = 0
for i in range(2 ** M):
    tmp = set()
    for j in range(M):
        if i >> j & 1:
            tmp = tmp | A[j]
    if len(tmp) == N:
        cnt += 1
print(cnt)
