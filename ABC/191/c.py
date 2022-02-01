h, w = map(int, input().split())
a = []
for _ in range(h):
    s = list(input())
    a.append(s)
ans = 0

for i in range(h-1):
    for j in range(w-1):
        cnt = 0
        if a[i][j] == '.':
            cnt += 1
        if a[i][j+1] == '.':
            cnt += 1
        if a[i+1][j] == '.':
            cnt += 1
        if a[i+1][j+1] == '.':
            cnt += 1
        if cnt % 2 == 1:
            ans += 1

print(ans)
