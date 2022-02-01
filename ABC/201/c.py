s = list(input())
ans = 0
for i in range(10000):
    tmp = list(str(i).zfill(4))
    for j in range(10):
        if s[j] == 'o':
            if not str(j) in tmp:
                break
        elif s[j] == 'x':
            if str(j) in tmp:
                break
    else:
        ans += 1

print(ans)
