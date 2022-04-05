T = int(input())
for i in range(T):
    print("Case #{}:".format(i + 1), end=" ")
    C1, M1, Y1, K1 = map(int, input().split())
    C2, M2, Y2, K2 = map(int, input().split())
    C3, M3, Y3, K3 = map(int, input().split())
    minC = min(C1, C2, C3)
    minM = min(M1, M2, M3)
    minY = min(Y1, Y2, Y3)
    minK = min(K1, K2, K3)
    if (minC + minM + minY + minK)  < 10 ** 6:
        print("IMPOSSIBLE")
    else:
        minl = [minC, minM, minY, minK]
        ans = [0, 0, 0, 0]
        for i in range(4):
            ans[i] = minl[i]
            if sum(ans) >= 10 ** 6:
                for j in range(4):
                    if j != i:
                        print(ans[j], end=" ")
                    else:
                        print(10 ** 6 - sum(ans) + ans[i], end=" ")
                print()
                break