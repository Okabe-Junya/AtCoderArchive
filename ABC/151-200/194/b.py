n = int(input())
xy = [map(int,input().split()) for i in range (n)]
x ,y = [list(i) for i in zip(*xy)]
l = []
for i in range(n):
    for j in range(n):
        if not i == j:
            l.append(max(x[i],y[j]))
        else:
            l.append(x[i]+y[j])
print(min(l))