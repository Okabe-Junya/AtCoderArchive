N = int(input())
a = list(map(int, input().split()))
tmp = 0
tmp2 = 0
for i in range(N):
    if a[i] == i + 1:
        tmp += 1
    elif a[a[i] - 1] == i + 1:
        tmp2 += 1
print(tmp * (tmp - 1) // 2 + tmp2 // 2)