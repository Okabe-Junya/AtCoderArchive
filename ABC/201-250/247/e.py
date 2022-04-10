N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
L = []
tmp = []
for i in range(N):
    if Y <= A[i] <= X:
        tmp.append(A[i])
    else:
        L.append(tmp)
        tmp = []
L.append(tmp)

ans = 0
for tmp_list in L:
    # 尺取法
    l = r = 0
    while l < len(tmp_list):
        Xflag = False
        Yflag = False
        while (not (Xflag and Yflag)) and r != len(tmp_list):
            if tmp_list[r] == X:
                Xflag = True
            if tmp_list[r] == Y:
                Yflag = True
            r += 1
        ans += len(tmp_list) - r
        l += 1
print(ans)
