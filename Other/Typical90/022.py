def gcd(m,n):
    r = m % n
    return gcd(n,r) if r else n
a, b, c= map(int,input().split())
g2 = gcd(a,b)
g = gcd(g2,c)
print((a//g)+(b//g)+(c//g) -3)