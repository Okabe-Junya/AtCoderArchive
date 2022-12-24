H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def koritu(i, j) -> bool:
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for di, dj in d:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= H or nj < 0 or nj >= W:
            continue
        if A[ni][nj] == A[i][j]:
            return False
    return True


def rv(i):
    A[i] = [1 - a for a in A[i]]


ans = 0
rvl = []
for i in range(H):
    # print(i + 1)
    flag = False
    for j in range(W):
        if koritu(i, j):
            ans += 1
            # print((i, j))
            if flag:
                print(-1)
                exit()
            flag = True
            rv(i)
            rvl.append(i)
            if i == 0:
                continue
            for k in range(W):
                if koritu(i - 1, k):
                    print(-1)
                    exit()

for i in range(len(rvl) - 1):
    if rvl[i] + 2 == rvl[i + 1]:
        flag = True
        for j in range(3):
            rv(rvl[i] + j)
        for j in range(-2, 3):
            if rvl[i] + j + 1 < 0 or rvl[i] + j + 1 >= H:
                continue
            for k in range(W):
                if koritu(rvl[i] + j + 1, k):
                    break
            else:
                flag = False
                break
        if flag:
            ans -= 1
        else:
            for j in range(3):
                rv(rvl[i] + j + 1)

print(min(ans, H - ans))
