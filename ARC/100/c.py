import statistics
n = int(input())
a = list(map(int,input().split()))
l = []
for i in range(n):
    tmp = a[i] - (i + 1)
    l.append(tmp)
a = round(statistics.median(l))
ans = 0
for i in l:
    ans += abs(i-a)
print(ans)