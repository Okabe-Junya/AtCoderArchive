s = input()
a = list(s)
b = a[0]
c = a[1]
d = a[2]
if b == 'S':
    if c == 'S':
        if d == 'S':
            print(0)
        else:
            print(1)
    else:
        if d == 'S':
            print(1)
        else:
            print(2)
else:
    if c == 'S':
        print(1)
    elif d == 'S':
        print(2)
    else:
        print(3)
