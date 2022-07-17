from bisect import bisect_left

N, K = map(int, input().split())
P = list(map(int, input().split()))
if K == 1:
    ans = [-1] * N
    for i in range(N):
        ans[P[i] - 1] = i + 1
    
    for i in ans:
        print(i)
    exit()

ans = [-1] * N
cnt = []
tmp = []
for i in range(N):
    p = bisect_left(tmp, P[i])
    if p == len(tmp):
        tmp.append(P[i])
        cnt.append([P[i]])
    else:
        tmp[p] = P[i]
        cnt[p].append(P[i])
        if len(cnt[p]) == K:
            for j in cnt[p]:
                ans[j - 1] = i + 1
            cnt.pop(p)
            tmp.pop(p)
for i in ans:
    print(i)