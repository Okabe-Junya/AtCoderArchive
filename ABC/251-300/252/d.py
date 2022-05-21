import bisect

# 二分探索（lower_bound）
def lower_bound(num_list, ky):
    pl = bisect.bisect_left(num_list, ky)
    pr = bisect.bisect_right(num_list, ky)
    return pr

N = int(input())
A = list(map(int, input().split()))

ans = 0
dict = {}
for i in range(N):
    if A[i] not in dict:
        dict[A[i]] = [i]
    else:
        dict[A[i]].append(i)

ans = N * (N - 1) * (N - 2) // 6
for i in dict:
    leng = len(dict[i])
    if leng >= 2:
        tmp = leng * (leng - 1) // 2
        tmp *= N - leng
        ans -= tmp
    if leng >= 3:
        tmp = leng * (leng - 1) * (leng - 2) // 6
        ans -= tmp
print(ans)