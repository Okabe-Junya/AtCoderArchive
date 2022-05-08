N, Q = map(int, input().split())
ans = [i for i in range(1, N + 1)]
idx = [i for i in range(N)]
for _ in range(Q):
    x = int(input())
    if ans[-1] == x:
        idx[x - 1] -= 1
        idx[ans[-2] - 1] += 1
        ans[-2], ans[-1] = ans[-1], ans[-2]
        continue
    p = idx[x - 1]
    idx[x - 1] += 1
    idx[ans[p + 1] - 1] -= 1
    ans[p], ans[p + 1] = ans[p + 1], ans[p]
print(*ans)