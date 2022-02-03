n = list(input())
for i in range(len(n)):
    if n[-1] == '0':
        n.pop()
    else:
        break
s = []
g = []
for i in range(len(n)):
    s.append(n[i])
    g.append(n[len(n)-1-i])
if s == g:
    print('Yes')
else:
    print('No')
