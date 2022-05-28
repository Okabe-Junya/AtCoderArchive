H, W = map(int, input().split())
l = []
for _ in range(H):
    l.append(list(input()))

o1 = [0, 0]
o2 = [0, 0]
cnt = 0
for i in range(H):
    for j in range(W):
        if l[i][j] == 'o' and cnt == 0:
            o1 = [i, j]
            cnt += 1
        elif l[i][j] == 'o' and cnt == 1:
            o2 = [i, j]
ans = 0
print(abs(o1[0] - o2[0]) + abs(o1[1] - o2[1]))