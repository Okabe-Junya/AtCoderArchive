num = list(map(int, input().split()))
a = num[0]
b = num[1]
c = num[2]
d = num[3]
e = a*c
f = a*d
g = b*c
h = b*d
nlist = [e, f, g, h]
print(max(nlist))
