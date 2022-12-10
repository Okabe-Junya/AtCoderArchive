N = int(input())
a = list(map(int, input().split()))
a = list(set(a))
a.sort(reverse=True)
A = []
for i in range(N):
    tmp = bin(a[i])[2:]
    A.append(tmp.zfill(30))

# min_max xor
for i in range(30):
    cnt0 = 0
    cnt1 = 0
    for j in range(N):
        if A[j][i] == '1':
            cnt1 += 1
        else:
            cnt0 += 1
    if cnt0 == 0 or cnt0 == N:
        continue
