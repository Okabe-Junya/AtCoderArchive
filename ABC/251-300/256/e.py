N = int(input())
X = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
cnt = [[i, 0] for i in range(N)]
for i in range(N):
    cnt[X[i] - 1][1] += C[i]
cnt.sort(key=lambda x: x[1])
print(cnt)
l = []
for i in range(N):
    l.append(cnt[i][0])

tmp_set = set()
for i in range(N):
    if X[l[i]] - 1 in tmp_set:
        ans += C[l[i]]
    tmp_set.add(l[i])
print(ans)