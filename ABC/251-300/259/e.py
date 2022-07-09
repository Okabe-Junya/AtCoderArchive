N = int(input())
L = []
for _ in range(N):
    m = int(input())
    tmp = []
    for _ in range(m):
        p, e = map(int, input().split())
        tmp.append((p, e))
    L.append(tmp)

lcm = {}
for i in range(N):
    for j in range(len(L[i])):
        if L[i][j][0] not in lcm:
            lcm[L[i][j][0]] = [{i}, L[i][j][1]]
        else:
            if lcm[L[i][j][0]][1] < L[i][j][1]:
                lcm[L[i][j][0]] = [{i}, L[i][j][1]]
            elif lcm[L[i][j][0]][1] == L[i][j][1]:
                lcm[L[i][j][0]][0].add(i)

ans_set = set()
for i in range(N):
    tmp_list = []
    for j in range(len(L[i])):
        if (i in lcm[L[i][j][0]][0]) and len(lcm[L[i][j][0]][0]) == 1:
            tmp_list.append(L[i][j][0])
    ans_set.add(tuple(tmp_list))
print(len(ans_set))