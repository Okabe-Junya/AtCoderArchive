s = list(input())
n = ''
for i in range(5):
    if s[0] == ' ':
        s.pop(0)
        break
    else:
        n += s[0]
        s.pop(0)
n = int(n)
ans = 0
for i in range(n-1):
    t = [0, 0, 0, 0]
    for j in range(i, n):
        if s[j] == 'A':
            t[0] += 1
        elif s[j] == 'T':
            t[1] += 1
        elif s[j] == 'G':
            t[2] += 1
        else:
            t[3] += 1
        if t[0] == t[1] and t[2] == t[3]:
            ans += 1
print(ans)
