a = list(map(int, input().split()))
ans = 0
a1 = a[0] % 2
b1 = a[1] % 2
c1 = a[2] % 2
if a1 + b1 + c1 == 1:
    ans += 1
    for i in range(3):
        if a[i] % 2 == 0:
            a[i] += 1

elif a1 + b1 + c1 == 2:
    ans += 1
    for i in range(3):
        if a[i] % 2 != 0:
            a[i] += 1
l = max(a)
ans += (l - a[0]) // 2 + (l - a[1]) // 2 + (l - a[2]) // 2
print(ans)
