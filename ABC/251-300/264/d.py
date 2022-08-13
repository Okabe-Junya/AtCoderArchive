S = list(input())
S2 = 'atcoder'
ans = 0

for i in range(len(S)):
    if S[i] == S2[i]:
        continue
    start = S.index(S2[i])
    while S[i] != S2[i]:
        S[start], S[start - 1] = S[start - 1], S[start]
        ans += 1
        start -= 1
print(ans)
