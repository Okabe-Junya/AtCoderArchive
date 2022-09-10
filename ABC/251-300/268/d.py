from itertools import permutations as p
from itertools import combinations as c

N, M = map(int, input().split())
S = []
T = set()
for _ in range(N):
    S.append(input())
for _ in range(M):
    tmp = input()
    T.add(tmp)
    # tmp = tmp.replace('_', '')
    # T.add(tmp)

cnt = 0
for j in range(N):
    cnt += len(S[j])

if N == 1:
    if len(S[0]) < 3:
        print('-1')
        exit()
    if S[0] not in T:
        print(S[0])
    else:
        print('-1')
    exit()


for i in p(S, N):
    cnt2 = cnt
    for s in range(N - 1, 17 - cnt2): # sこの_を入れる
        for j in c(range(1, s), N - 2):
            if N - 2 == 0:
                j2 = [s]
            else:
                j2 = [j[0]]
                for j3 in range(len(j) - 1):
                    j2.append(j[j3 + 1] - j[j3])
                j2.append(s - j[-1])
            tmp = ''
            tmp += i[0]
            for k in range(len(j2)):
                tmp += '_' * j2[k]
                tmp += i[k + 1]
            # print(tmp, i, j2, s)
            if (tmp not in T) and (3 <= len(tmp) <= 16):
                print(tmp)
                exit()
print('-1')

