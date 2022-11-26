from bisect import bisect_left


N, M = map(int, input().split())
A = list(map(int, input().split()))

Adict = {}
for i in range(M):
    if A[i] in Adict:
        Adict[A[i]].append(i)
    else:
        Adict[A[i]] = [i]

print(Adict)

for i in range(M):
    ans = 1
    # for j in range(M):
    #     if i == j:
    #         continue
    #     if A[j] == ans:
    #         ans += 1
    #     elif A[j] == ans - 1:
    #         ans -= 1
    j = 0
    while True:
        p1 = -1
        p2 = -1
        if j == M:
            break
        if ans in Adict:
            p1 = bisect_left(Adict[ans], j)
            if p1 == len(Adict[ans]):
                p1 = -1
        if ans - 1 in Adict:
            p2 = bisect_left(Adict[ans - 1], j)
            if p2 == len(Adict[ans - 1]):
                p2 = -1

        if p1 == p2 == -1:
            break

        if p1 == -1:
            j = p2 + 1
            ans -= 1
        elif p2 == -1:
            j = p1 + 1
            ans += 1
        else:
            if p1 < p2:
                j = p1 + 1
                ans += 1
            else:
                j = p2 + 1
                ans -= 1
        print(ans, j)
    print(ans)
