a, b = map(int, input().split())
d = b - a
ans = 1
if a % d == 0:
    print(d)
    exit()
for i in range(d-1, 0, -1):
    if (a % i) - (b % i) > 0 or a % i == 0:
        print(i)
        break
else:
    print(1)
