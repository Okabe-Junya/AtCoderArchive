S = input()
if S[0] != S[1] and S[0] != S[2]:
    print(S[0])
    exit()
elif S[0] != S[1] and S[1] != S[2]:
    print(S[1])
    exit()
elif S[0] != S[2] and S[1] != S[2]:
    print(S[2])
    exit()
else:
    print(-1)