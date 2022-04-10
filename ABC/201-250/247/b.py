N = int(input())
l = []
for i in range(N):
    s, t = input().split()
    l.append((s, t))

for i in range(N):
    flag = False
    for j in range(2):
        tmp = l[i][j]
        for k in range(N):
            if (k != i) and (tmp in l[k]):
                break
        else:
            flag = True
    if not flag:
        print("No")
        exit()
print("Yes")
