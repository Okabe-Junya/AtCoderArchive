

S = []
for _ in range(9):
    S.append(list(input()))

ans = 0


def check(p1, p2, p3, p4):
    # 与えられた4点が正方形か否か判定する．
    # 4点が正方形ならTrueを返す．
    if p1[0] == p2[0]:
        # p1とp2が同じx座標を持つ
        if p3[0] == p4[0]:
            # p3とp4も同じx座標を持つ
            if p1[1] == p3[1]:
                # p1とp3が同じy座標を持つ
                if p2[1] == p4[1]:
                    # p2とp4も同じy座標を持つ
                    if p1[1] - p2[1] == p3[1] - p4[1]:
                        # p1とp2のx座標の差とp3とp4のy座標の差が等しい
                        return True
                    else:
                        return False
    else:
        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p3[0] - p1[0], p3[1] - p1[1])
        if v1[0] ** 2 + v1[1] ** 2 == v2[0] ** 2 + v2[1] ** 2:
            # p1, p2, p3が直角三角形
            v3 = (p4[0] - p1[0], p4[1] - p1[1])
            if v1[0] * v3[0] + v1[1] * v3[1] == 0:
                # p1, p2, p4が直角三角形
                return True
    return False





for i in range(81 - 3):
    for j in range(i + 1, 81 - 2):
        for k in range(j + 1, 81 - 1):
            for l in range(k + 1, 81):
                p1 = (i // 9, i % 9)
                p2 = (j // 9, j % 9)
                p3 = (k // 9, k % 9)
                p4 = (l // 9, l % 9)
                if (
                    S[p1[0]][p1[1]] == "#"
                    and S[p2[0]][p2[1]] == "#"
                    and S[p3[0]][p3[1]] == "#"
                    and S[p4[0]][p4[1]] == "#"
                ):
                    if check(p1, p2, p3, p4):
                        print(p1, p2, p3, p4)
                        ans += 1

print(ans)
