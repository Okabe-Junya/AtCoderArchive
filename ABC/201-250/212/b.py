l = list(input())

if l[0] == l[1] and l[1] == l[2] and l[2] == l[3]:
    print("Weak")
else:
    a = int(l[0])
    for i in range(3):
        if a == 9:
            a = -1
        if int(l[i+1]) != a + 1:
            print("Strong")
            break
        a = int(l[i+1])

    else:
        print("Weak")
