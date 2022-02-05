n = int(input())
a = list(map(int, input().split()))
l = [False] * 360
l[0] = True
tmp = 0
for i in range(n):
    tmp += a[i]
    l[tmp % 360] = True
    tmp %= 360

ans = []
cnt = 0
l = l + l
for i in l:
    if i == False:
        cnt += 1
    else:
        ans.append(cnt + 1)
        cnt = 0
#print(ans)
print(max(ans))