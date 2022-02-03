n, m = map(int, input().split())
h = list(map(int, input().split()))
xy = [map(int, input().split()) for i in range(m)]
x, y = [list(i) for i in zip(*xy)]
ans = [True for _ in range(n)]
for i in range(m):
    if h[x[i]-1] > h[y[i]-1]:
        ans[y[i]-1] = False
    elif h[x[i]-1] == h[y[i]-1]:
        ans[y[i]-1] = False
        ans[x[i]-1] = False
    else:
        ans[x[i]-1] = False
cnt = 0
for i in ans:
    if i:
        cnt += 1
print(cnt)
