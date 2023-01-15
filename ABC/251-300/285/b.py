N = int(input())
S = input()
for i in range(N - 1):
    p = 0
    start = i + 1
    ans = 0
    while start < N:
        # print(S[i], S[start])
        if S[p] != S[start]:
            ans += 1
            start += 1
            p += 1
        else:
            break
    print(ans)
