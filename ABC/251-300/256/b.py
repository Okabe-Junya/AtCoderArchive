N = int(input())
A = list(map(int, input().split()))
tmp = [0, 0, 0, 0]
ans = 0
for i in range(N):
    tmp[0] = 1
    for j in range(3, -1, -1):
        if tmp[j] != 0:
            if j + A[i] < 4:
                tmp[j + A[i]] += tmp[j]
            else:
                ans += tmp[j]
            tmp[j] = 0
print(ans)