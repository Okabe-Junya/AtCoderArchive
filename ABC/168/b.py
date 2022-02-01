k = int(input())
s = list(input())
if len(s) > k:
    for i in range(k):
        print(s[i], end='')
    print('...')
else:
    for i in s:
        print(i, end='')
