x, y, a, b = map(int, input().split())
ans = 0

for i in range(10**18):
    if x*a >= x+b or x*a >= y:
        break
    x = x*a
    ans += 1

print(ans+(y-1-x)//b)
