n, k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
l.sort()
cnt = 0
for i in range(n):
    cnt += l[i][1]
    if cnt >= k:
        print(l[i][0])
        break
else:
    print(l[-1][0])
