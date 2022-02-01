x, k, d = map(int, input().split())
if x > 0:
    if x > k * d:
        print(x - k * d)
    else:
        k -= x // d
        x = x % d
        if k % 2 == 0:
            print(x)
        else:
            print(abs(x-d))
elif x < 0:
    if -x > k * d:
        print(abs(x + k * d))
    else:
        k -= -x // d
        x += (-x // d) * d
        if k % 2 == 0:
            print(-x)
        else:
            if x > 0:
                print(abs(x-d))
            else:
                print(abs(x+d))
else:
    if k % 2 == 0:
        print(0)
    else:
        print(d)
