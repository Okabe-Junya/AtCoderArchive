N = int(input())
P = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    # print(P[i - 1], P[i])
    if P[i] < P[i - 1]:
        tmpmax = 0
        for j in range(i, N):
            if P[j] > tmpmax and P[j] < P[i - 1]:
                tmpmax = P[j]
                tmpidx = j
        idx = P.index(P[i - 1])
        idx2 = P.index(tmpmax)
        P[idx], P[idx2] = P[idx2], P[idx]
        L = []
        for j in range(idx + 1, N):
            L.append(P[j])
        L.sort(reverse=True)
        break

# print(L)
# print(P)
for i in range(N):
    if i < idx + 1:
        print(P[i], end=' ')
    else:
        print(L[i - idx - 1], end=' ')
print()
