S = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if len(S) != 8:
    print('No')
    exit()
if S[0] in alphabet and S[-1] in alphabet:
    if S[1:7].isdigit():
        if int(S[1:7]) >= 100000:
            print('Yes')
            exit()
print('No')
