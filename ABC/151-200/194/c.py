n = int(input())
x = list(map(int, input().split()))
l = [0]
for i in range(n):
    l.append(l[-1]+x[i])
ans = 0
for i in range(1, n):
    ans += i * (x[i] ** 2)
    ans += (n-i) * (x[i-1] ** 2)
    ans -= 2 * x[i] * l[i]
print(ans)
