n = int(input())
a = list(map(int, input().split()))
tmp = 0
for i in range(n):
    tmp = tmp ^ a[i]
for i in range(n):
    print(tmp ^ a[i], end=' ')
