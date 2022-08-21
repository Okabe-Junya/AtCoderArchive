from bisect import bisect_left


N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
Asum = [0]
for i in range(N):
    Asum.append(Asum[-1] + A[i])

for i in range(N):
    pl1 = bisect_left(Asum, P + Asum[i])
    if pl1 > N:
        continue
    if Asum[pl1] == P + Asum[i]:
        pl2 = bisect_left(Asum, Q + Asum[pl1])
        if pl2 > N:
            continue
        if Asum[pl2] == Q + Asum[pl1]:
            pl3 = bisect_left(Asum, R + Asum[pl2])
            if pl3 > N:
                continue
            if Asum[pl3] == R + Asum[pl2]:
                print('Yes')
                exit()
print('No')        
