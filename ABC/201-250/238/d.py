T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    if 2 * a > s:
        print('No')
        continue
    
    d = s - 2 * a
    l = [False] * 60
    b = list(str(bin(a)[2:]))
    for i in range(len(b)):
        if b[i] == '1':
            l[i] = True
    b2 = list(str(bin(d)[2:]))
    b2.reverse()
    print(l)
    print(b2)
    for i in range(len(b2)):
        if (b2[i] == '1') & (l[i] == True):
            print('No')
            break
    else:
        print("Yes")
    