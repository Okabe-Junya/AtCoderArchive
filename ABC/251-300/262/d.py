INF = 998244353

N = int(input())
a = list(map(int, input().split()))
dict = {}

ans = 0
for i in range(N):
    tmp = [a[0] % (i + 1)]
    tmpsum = [a[0] % (i + 1)]
    for j in range(1, N):
        tmp.append(a[j] % (i + 1))
        tmpsum.append(tmpsum[-1] + a[j] % (i + 1))
        dict[i + 1] = tmpsum

for key in dict:
    l = dict[key]
    print(key, l)
    
print(ans)