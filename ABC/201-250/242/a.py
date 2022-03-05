a, b, c, x = map(int, input().split())
if x <= a:
    print(1)
    exit()
elif x <= b:
    print(c / (b - a))
    exit()
else:
    print(0)
