H, W = map(int, input().split())
S = []
T = []
for i in range(H):
    S.append(input())

for i in range(H):
    T.append(input())

Sl = []
Tl = []
for i in range(W):
    tmps = []
    tmpt = []
    for j in range(H):
        tmps.append(S[j][i])
        tmpt.append(T[j][i])
    Sl.append(tmps)
    Tl.append(tmpt)

Sl.sort()
Tl.sort()

for i in range(W):
    if Sl[i] != Tl[i]:
        print('No')
        exit()
print('Yes')
