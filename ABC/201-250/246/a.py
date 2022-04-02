x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

l = [(x1, y1), (x2, y2), (x3, y3)]

ansx = []
ansy = []
for i in range(3):
    if l[i][0] not in ansx:
        ansx.append(l[i][0])
    else:
        ansx.remove(l[i][0])
    if l[i][1] not in ansy:
        ansy.append(l[i][1])
    else:
        ansy.remove(l[i][1])
print(ansx[0], ansy[0])