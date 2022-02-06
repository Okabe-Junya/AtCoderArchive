n, m = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
c = x + y
d = []
s = x
for i in x:
    if i in y:
        d.append(i)
for j in set(c):
    if j not in d:
        print(j,end=' ')


