h, w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]
row_sum = []
column_sum = [0 for _ in range(w)]
for i in a:
    row_sum.append(sum(i))
    for j in range(w):
        column_sum[j] += i[j]

for i in range(h):
    for j in range(w):
        print(row_sum[i] + column_sum[j] - a[i][j], end = ' ')
    print('')