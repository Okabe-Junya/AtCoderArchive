S = input()
S = list(S)
ans = 0
while True:
    if len(S) < 2:
        ans += 1
        break
    elif S[-1] == S[-2] == '0':
        ans += 1
        S.pop()
        S.pop()
    else:
        ans += 1
        S.pop()
print(ans)
