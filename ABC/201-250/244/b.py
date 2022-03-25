N = int(input())
T = list(input())
d = 0
dl = [[1, 0], [0, -1], [-1, 0], [0, 1]]
tmp = [0, 0]
for i in range(N):
    if T[i] == 'S':
        tmp[0] += dl[d][0]
        tmp[1] += dl[d][1]
    else:
        d += 1
        d %= 4

for i in tmp:
    print(i, end=' ')