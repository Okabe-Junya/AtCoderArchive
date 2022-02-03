n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(b[c[i-1]-1])
cnt = [0 for _ in range(n)]
cnt2 = [0 for _ in range(n)]
for i in range(n):
    cnt[a[i]-1] += 1
    cnt2[l[i]-1] += 1
ans = 0
for j in range(n):
    ans += cnt[j] * cnt2[j]
print(ans)
