n = int(input())
a2 = list(map(int,input().split()))
b2 = list(map(int,input().split()))
c2 = list(map(int,input().split()))
    
a = [0 for _ in range(46)]    
b = [0 for _ in range(46)]
c = [0 for _ in range(46)]
ans = 0

for i in range(n):
    a[a2[i]%46] += 1
    b[b2[i]%46] += 1
    c[c2[i]%46] += 1

for i in range(46):
    for j in range(46):
        k = (46 - i - j) % 46
        ans += a[i] * b[j] * c[k]
        
print(ans)