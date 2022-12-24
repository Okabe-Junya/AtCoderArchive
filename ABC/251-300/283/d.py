from collections import deque

S = input()
alphabet = {}
lens = len(S)
ll = []
rl = []
for i in range(lens):
    if S[i] == "(":
        ll.append(i)
    elif S[i] == ")":
        rl.append(i)

if not ll:
    tmpset = set()
    for i in range(lens):
        if S[i] in tmpset:
            print("No")
            exit()
        tmpset.add(S[i])
    print("Yes")
    exit()

ll = ll[::-1]
tmp = S[ll[0]+1: rl[0]]
pl = ll[0]
pr = rl[0]
alphabet[rl[0]] = tmp
for i in range(len(ll) - 1):
    while pl > ll[i + 1]:
        pl -= 1
        if S[pl] == ")" or S[pl] == "(":
            continue
        tmp = S[pl] + tmp
    while pr < rl[i + 1]:
        pr += 1
        if S[pr] == ")" or S[pr] == "(":
            continue
        tmp += S[pr]
    alphabet[rl[i + 1]] = tmp

# print(alphabet)

for i in alphabet:
    tmp = ''
    for j in alphabet[i]:
        if j == "(" or j == ")":
            continue
        else:
            tmp += j
    alphabet[i] = tmp

# print(alphabet)

tmpset = set()
for i in range(lens):
    if S[i] == "(":
        continue
    elif S[i] == ")":
        for j in alphabet[i]:
            tmpset.discard(j)
    else:
        if S[i] in tmpset:
            print("No")
            exit()
        tmpset.add(S[i])
print("Yes")
