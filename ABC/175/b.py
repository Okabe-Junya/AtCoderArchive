n = int(input())
l = list(map(int, input().split()))
ans = 0
if n <= 2:
    print(0)
    exit()
if n == 3:
    if 2 * max(l) < sum(l):
        print(1)
        exit()
    else:
        print(0)
        exit()
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            row = []
            row.append(l[i])
            if l[i] == l[j]:
                continue
            row.append(l[j])
            if l[i] == l[k] or l[j] == l[k]:
                continue
            row.append(l[k])
            if 2 * max(row) < sum(row):
                ans += 1
print(ans)
