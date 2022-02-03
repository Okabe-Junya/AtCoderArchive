n = int(input())
a = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(a[i] % 200)
ans = 0
for i in range(200):
    tmp = 0
    for j in range(n):
        if l[j] == i:
            tmp += 1
    ans += tmp * (tmp - 1) // 2
print(ans)
