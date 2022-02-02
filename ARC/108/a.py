import math
s, p = map(int, input().split())
t = s ** 2 - 4 * p
if t < 0:
    print('No')
elif t == 0:
    print('Yes')
else:
    w = math.sqrt(t)
    if round(w) == 0:
        print('No')
    elif t % round(w) == 0:
        print('Yes')
    else:
        print('No')
