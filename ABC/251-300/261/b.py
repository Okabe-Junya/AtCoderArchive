N = int(input())
A = []
for _ in range(N):
    A.append(list(input()))


for i in range(N):
    for j in range(N):
        if (A[i][j] == 'W') and (not (A[j][i] == 'L')):
            print('incorrect')
            exit()
        elif (A[i][j] == 'L') and (not (A[j][i] == 'W')):
            print('incorrect')
            exit()
        elif (A[i][j] == 'D') and (not (A[j][i] == 'D')):
            print('incorrect')
            exit()
print('correct')
            