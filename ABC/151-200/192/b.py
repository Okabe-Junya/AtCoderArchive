s = list(input())
for i in range(len(s)):
    if i % 2 == 0:
        if not s[i].islower():
            print('No')
            break
    else:
        if not s[i].isupper():
            print('No')
            break
else:
    print('Yes')
