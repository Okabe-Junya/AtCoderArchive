from decimal import Decimal
n ,x= map(int,input().split())
cnt = 0
for i in range(n):
    v, p = map(int,input().split())
    v = Decimal(str(v))
    p = Decimal(str(p))
    cnt += v * p / 100
    if cnt > x:
        print(i+1)
        break
else:
    print(-1)