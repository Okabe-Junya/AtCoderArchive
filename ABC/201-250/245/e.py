import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
CHO = []
BOX = []
for i in range(N):
    CHO.append([A[i], B[i]])
for i in range(M):
    BOX.append([C[i], D[i]])
CHO.sort()
BOX.sort()
# print(CHO)
# print(BOX)


def lower_bound(num_list, ky):
    pl = bisect.bisect_left(num_list, ky)
    # pr = bisect.bisect_right(num_list, ky)
    return pl


b = [False] * M
