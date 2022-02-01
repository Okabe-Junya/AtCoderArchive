s = list(input())
for i in range(len(s)):
    if s[len(s)-i-1] == '0' or s[len(s)-i-1] == '1' or s[len(s)-i-1] == '8':
        print(int(s[len(s)-i-1]), end='')
    elif s[len(s)-i-1] == '6':
        print(9, end='')
    else:
        print(6, end='')
