# ABC122-B
s = list(input())
l = []
for i in s:
    if i == 'A' or i == 'C' or i == 'G' or i == 'T':
        a = 1
    else:
        a = 0
    l.append(a)
m = []
cnt = 0
for i in range(len(l)):
    if l[i] == 1:
        cnt += 1
        if i == len(l) - 1:
            m.append(cnt)
    else:
        m.append(cnt)
        cnt = 0
print(max(m))
