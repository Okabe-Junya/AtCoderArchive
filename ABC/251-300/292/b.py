N, Q = map(int, input().split())
tmp = [0] * N
for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        tmp[x - 1] += 1
    elif c == 2:
        tmp[x - 1] += 2
    else:
        if tmp[x - 1] >= 2:
            print("Yes")
        else:
            print("No")
