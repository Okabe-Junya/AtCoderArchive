# ABC095-C
a, b, c, x, y = map(int, input().split())
ans = 0
if x - y >= 0:
    bool_x = True
else:
    bool_x = False

if a + b > 2 * c:
    ans += min(x, y) * 2 * c
    if bool_x:
        ans += (x - min(x, y)) * min(a, 2 * c)
    else:
        ans += (y - min(x, y)) * min(b, 2 * c)
    print(ans)

else:
    print(a * x + b * y)