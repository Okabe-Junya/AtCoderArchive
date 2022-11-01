S = []
for _ in range(9):
    S.append(list(input()))

ans = 0


def check(p1, p2, p3, p4):
    L = []
    from itertools import combinations as cmb

    for l1, l2 in cmb((p1, p2, p3, p4), 2):
        L.append((l1[0] - l2[0]) ** 2 + (l1[1] - l2[1]) ** 2)
        L.sort()
    if L[0] == L[1] == L[2] == L[3]:
        if L[-1] == L[-2]:
            if L[-1] == 2 * L[0]:
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
                        ans += 1

print(ans)
