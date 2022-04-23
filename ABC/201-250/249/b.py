S = input()
if len(S) == len(set(S)):
    a = False
    b = False
    for i in S:
        if i == i.upper():
            a = True
        if i == i.lower():
            b = True
    if a and b:
        print("Yes")
        exit()
print("No")