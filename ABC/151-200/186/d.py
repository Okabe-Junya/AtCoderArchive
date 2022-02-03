n = int(input())
a = list(map(int, input().split()))
cnt = 0
a.sort()
for i in range(len(a)):
    cnt += a[i] * (2 * i - (len(a)-1))
print(cnt)
