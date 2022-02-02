a, b, x, y = map(int, input().split())
if a < b:
    if y <= 2 * x:
        print(y * (b-a) + x)
    else:
        print(x * (2 * (b - a) + 1))
elif a == b:
    print(x)
else:
    if y <= 2 * x:
        print(y * (a - b - 1) + x)
    else:
        print(x * ((2 * (a - b) - 1)))
