n = int(input())
l = list(str(n))
s = len(l)
ans = 0
if s == 1:
    print(0)
    exit()
if s % 2 != 0:
    l = ['9' for _ in range(s-1)]
    s -= 1
tmp = s // 2
m = ''
k1 = ''
for j in range(tmp):
    m += l[j]
    k1 += l[s-j-1]
k = k1[::-1]
ans += int(m)
if int(m) > int(k):
    ans -= 1
print(ans)
