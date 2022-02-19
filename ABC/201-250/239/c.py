x1, y1, x2, y2 = map(int, input().split())
l = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
tmp = []
for i in l:
    tmp.append((x1 + i[0], y1 + i[1]))

for i in l:
    t = (x2 + i[0], y2 + i[1])
    if t in tmp:
        print('Yes')
        exit()
else:
    print("No")