L = list(map(int, input().split()))
L.sort()
if ((L[0] == L[1] == L[2]) and (L[3] == L[4])) or ((L[0] == L[1]) and (L[2] == L[3] == L[4])):
    print('Yes')
else:
    print('No')