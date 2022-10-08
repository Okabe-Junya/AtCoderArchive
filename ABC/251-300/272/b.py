N, M = map(int, input().split())
L = []
for i in range(M):
    tmp = list(map(int, input().split()))
    tmp.pop(0)
    L.append(set(tmp))

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(M):
            if i + 1 in L[k] and j + 1 in L[k]:
                break
        else:
            print('No')
            exit()
print('Yes')
