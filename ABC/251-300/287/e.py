from bisect import bisect_left


N = int(input())
Sl = []
for i in range(N):
    S = input()
    Sl.append(S)

Slsort = sorted(Sl)
# print(Slsort)

for i in range(N):
    ans = 0
    S = Sl[i]
    p = bisect_left(Slsort, S)
    if p + 1 < N:
        tmp = 0
        while Slsort[p][tmp] == Slsort[p + 1][tmp]:
            tmp += 1
            if tmp == len(S):
                break
            if tmp == len(Slsort[p + 1]):
                break
        ans = max(ans, tmp)
    if p - 1 >= 0:
        tmp = 0
        while Slsort[p][tmp] == Slsort[p - 1][tmp]:
            tmp += 1
            if tmp == len(S):
                break
            if tmp == len(Slsort[p - 1]):
                break
        ans = max(ans, tmp)
    print(ans)
