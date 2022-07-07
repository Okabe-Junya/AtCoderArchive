N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))

for i in range(N):
    for j in range(N):
        A[i][j] = int(A[i][j])
    
ans_list = []
d = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))
for i in range(N):
    for j in range(N):
        for dx, dy in d:
            x, y = i, j
            tmp = str(A[i][j])
            for _ in range(N - 1):
                x += dx
                y += dy
                x %= N
                y %= N
                tmp += str(A[x][y])
            ans_list.append(tmp)
print(max(ans_list))