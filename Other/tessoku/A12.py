N, K = map(int, input().split())
A = list(map(int, input().split()))
pl = 0
pr = 10 ** 9
while pr > pl:
    # print(pl, pr)
    pm = (pl + pr) // 2
    if sum(pm // a for a in A) >= K:
        pr = pm
    else:
        pl = pm + 1
print(pl)
