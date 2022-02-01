n = int(input())
a = []
ans = 0
for _ in range(n):
    s = input()
    if s == 'AND':
        a.append(1)
    else:
        a.append(0)
for i in range(n):
    if a[i] == 0:
        ans += 2 ** (i+1)
print(ans + 1)
