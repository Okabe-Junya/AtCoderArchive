s = list(input().split('+'))
ans = 0
for i in s:
    l = list(i)
    if '0' not in l:
        ans += 1
print(ans)
