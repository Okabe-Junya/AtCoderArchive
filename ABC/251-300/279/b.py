S = input()
T = input()
if len(S) < len(T):
    print('No')
    exit()

# 部分文字列判定
for i in range(len(S) - len(T) + 1):
    for j in range(len(T)):
        if S[i + j] != T[j]:
            break
    else:
        print('Yes')
        exit()
print('No')
