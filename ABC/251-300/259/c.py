S = input()
T = input()

sl = []
pl = []
tmp = ""
cnt = 1
for i in S:
    if i == tmp:
        cnt += 1
    else:
        sl.append((tmp, cnt))
        tmp = i
        cnt = 1
sl.append((tmp, cnt))

tmp = ""
cnt = 1
for i in T:
    if i == tmp:
        cnt += 1
    else:
        pl.append((tmp, cnt))
        tmp = i
        cnt = 1
pl.append((tmp, cnt))


if len(sl) != len(pl):
    print("No")
    exit()
for i in range(len(sl)):
    if sl[i][1] < 2:
        if sl[i] != pl[i]:
            print("No")
            exit()
    else:
        if sl[i][0] != pl[i][0]:
            print("No")
            exit()
        elif sl[i][1] > pl[i][1]:
            print("No")
            exit()
print("Yes")