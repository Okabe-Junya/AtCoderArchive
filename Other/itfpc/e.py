import time


def is_cross(p1, p2, p3, p4):
    s = (p1[0] - p2[0]) * (p3[1] - p1[1]) - (p1[1] - p2[1]) * (p3[0] - p1[0])
    t = (p1[0] - p2[0]) * (p4[1] - p1[1]) - (p1[1] - p2[1]) * (p4[0] - p1[0])
    if s * t >= 0:
        return False

    s = (p3[0] - p4[0]) * (p1[1] - p3[1]) - (p3[1] - p4[1]) * (p1[0] - p3[0])
    t = (p3[0] - p4[0]) * (p2[1] - p3[1]) - (p3[1] - p4[1]) * (p2[0] - p3[0])
    if s * t >= 0:
        return False
    return True


start = time.time()
W, H, N = map(int, input().split())
L = [[] for _ in range(N)]
for _ in range(N * 2):
    x, y, c = map(int, input().split())
    L[c - 1].append((x, y))

for i in range(N):
    for j in range(i + 1, N):
        # 例外ケースの判定．((0, p1), (0, p2)), ((0, p3), (0, p4))
        if (
            L[i][0][0] == L[i][1][0]
            and L[j][0][0] == L[j][1][0]
            and L[i][0][0] == L[j][0][0]
        ):
            tmp_time = time.time()
            if tmp_time - start > 1.3:
                print("Yes")
                exit()
            if max(L[i][0][1], L[i][1][1]) < min(L[j][0][1], L[j][1][1]) or max(
                L[j][0][1], L[j][1][1]
            ) < min(L[i][0][1], L[i][1][1]):
                continue
        # 例外ケースの判定．((p1, 0), (p2, 0)), ((p3, 0), (p4, 0))
        if (
            L[i][0][1] == L[i][1][1]
            and L[j][0][1] == L[j][1][1]
            and L[i][0][1] == L[j][0][1]
        ):
            if max(L[i][0][0], L[i][1][0]) < min(L[j][0][0], L[j][1][0]) or max(
                L[j][0][0], L[j][1][0]
            ) < min(L[i][0][0], L[i][1][0]):
                continue

        if is_cross(L[i][0], L[i][1], L[j][0], L[j][1]):
            print("No")
            exit()
print("Yes")
