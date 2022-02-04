N, K = map(int, input().split())
a = []
b = []
c = []
ans = 0
for _ in range(N):
    an, bn = map(int, input().split())
    a.append(an)
    b.append(bn)
    c.append(an - bn)

l = b + c
l = sorted(l, reverse=True)
for i in range(K):
    ans += l[i]
    
print(ans)