n = int(input())
a = list(map(int, input().split()))
l = [0]
ans = 0
for i in range(n):
    if a[i] > l[-1]:
        l.append(a[i])
    else:
        ans += l[-1]-a[i]
print(ans)
