s = list(input())
l = len(s)
ans = 0
for i in range(1, l):
    if s[i] != s[i-1]:
        ans += 1
print(ans)
