n = int(input())
xy = [map(int, input().split()) for i in range(n)]
x, y = [list(i) for i in zip(*xy)]
cnt = 0
for i in range(len(x)):
    for j in range(i+1, len(x)):
        x_dif = x[i] - x[j]
        y_dif = y[i] - y[j]
        if -1 <= (y_dif/x_dif) <= 1:
            cnt += 1
print(cnt)
