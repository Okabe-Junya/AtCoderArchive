from math import floor

X = int(input())
tmp = list(str(X))
if 0 <= X <= 9:
    print(0)
    exit()
if -9 <= X <= -1:
    print(-1)
    exit()
if X >= 0:
    tmp.pop()
    print(int(''.join(tmp)))
else:
    if X % 10 == 0:
        tmp.pop()
        print(int(''.join(tmp)))
    else:
        tmp.pop()
        n = int(''.join(tmp))
        print(n - 1)