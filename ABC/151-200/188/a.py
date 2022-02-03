a ,b= map(int,input().split())
if a < b :
    a, b = b, a
if a - b < 3:
    print('Yes')
else:
    print('No')