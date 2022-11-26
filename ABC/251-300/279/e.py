from bisect import bisect_right


N, M = map(int, input().split())
A = list(map(int, input().split()))
Adict = {}
for i in range(M):
    if A[i] in Adict:
        Adict[A[i]].append(i)
    else:
        Adict[A[i]] = [i]

print(Adict)

for i in range(1):
    p = -1
    ans = 1
    p1 = -1
    p2 = -1
    while True:
        if p == N - 1:
            break
        print(p, ans)
        if (ans not in Adict) and (ans - 1 not in Adict):
            break
        if ans - 1 in Adict:
            p1 = bisect_right(Adict[ans - 1], p)
            if p1 == len(Adict[ans - 1]):
                p1 = -1
            elif p1 < len(Adict[ans - 1]):
                if Adict[ans - 1][p1] == i + 1:
                    p1 += 1
                if p1 == len(Adict[ans - 1]):
                    p1 = -1
        if ans in Adict:
            p2 = bisect_right(Adict[ans], p)
            if p2 == len(Adict[ans]):
                p2 = -1
        if p1 == -1 and p2 == -1:
            break
        if p1 == -1:
            p = p2
            ans += 1
        elif p2 == -1:
            p = p1
            ans -= 1
        else:
            if p1 < p2:
                p = p1
                ans -= 1
            else:
                p = p2
                ans += 1
    print(ans)
