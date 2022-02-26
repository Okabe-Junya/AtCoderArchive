N = int(input())
l = []
for _ in range(N):
    tmp = []
    S = input()
    for i in S:
        if i == ".":
            tmp.append(0)
        else:
            tmp.append(1)
    l.append(tmp)


# よこ
for i in range(N):
    tmp = sum(l[i][0:6])
    if tmp >= 4:
        print("Yes")
        exit()
    for j in range(N - 6):
        tmp += l[i][j + 6] - l[i][j]
        if tmp >= 4:
            print("Yes")
            exit()

# たて
for i in range(N):
    tmp = 0
    for j in range(6):
        tmp += l[j][i]
    if tmp >= 4:
        print("Yes")
        exit()
    for j in range(N - 6):
        tmp += l[j + 6][i] - l[j][i]
        if tmp >= 4:
            print("Yes")
            exit()
            
            
# ななめ
for i in range(N - 5):
    for j in range(N - 5):
        tmp = 0
        for k in range(6):
            tmp += l[i + k][j + k]
        if tmp >= 4:
            print("Yes")
            exit()


for i in range(N - 5):
    for j in range(N - 5):
        tmp = 0
        for k in range(6):
            tmp += l[i + k][j + 5 - k]
        if tmp >= 4:
            print("Yes")
            exit()

print("No")