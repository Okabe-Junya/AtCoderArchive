x = list(input())
s = ''
for i in x:
    if i == '.':
        print(int(s))
        break
    else:
        s += i
else:
    print(int(s))
