N = int(input())
S = list(input())
flag = True
for i in range(N):
    if S[i] == ',':
        if flag:
            S[i] = '.'
    elif S[i] == '"':
        flag = not flag
print(''.join(S))
