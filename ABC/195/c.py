n = int(input())
s = list(str(n))
l = len(s)
ans = 0
if l <= 3:
    print(0)

else:
    for i in range(3, l):
        ans += 9 * 10**i * (i//3)
    ans += (n-10**l) * ((l-1)//3)
    print(ans+((l-1)//3))
