N, M = map(int, input().split())
S = list(map(int, input().split()))
X = list(map(int, input().split()))
Xset = set(X)
Sn = [0]
for i in range(N - 1):
    Sn.append(S[i] - Sn[-1])

Sodd = []
Seven = []
for i in range(N):
    if i % 2 == 0:
        Seven.append(Sn[i])
    else:
        Sodd.append(Sn[i])

dict = {}
for i in range(len(Seven)):
    for j in Xset:
        if j - Seven[i] in dict:
            dict[j - Seven[i]] += 1
        else:
            dict[j - Seven[i]] = 1

for i in range(len(Sodd)):
    for j in Xset:
        if Sodd[i] - j in dict:
            dict[Sodd[i] - j] += 1
        else:
            dict[Sodd[i] - j] = 1

print(max(dict.values()))