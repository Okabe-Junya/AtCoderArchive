n, m  = map(int, input().split())

l = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    if a < b:
        l[b - 1] += 1
    elif a > b:
        l[a - 1] += 1

#print(l)
ans  = 0
for i in l:
    if i == 1:
        ans += 1
print(ans)