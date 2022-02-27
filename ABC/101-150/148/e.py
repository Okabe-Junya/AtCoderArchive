n = int(input())
if n % 2 == 1:
    print(0)
else:
    ans = 0
    while n != 0:
        tmp = n // 5
        ans += tmp // 2
        n = tmp
    print(ans)