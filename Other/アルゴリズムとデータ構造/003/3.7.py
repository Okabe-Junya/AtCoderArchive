S = input()
ans = 0
x = len(S) - 1
if x == 0:
    print(int(S))
    exit()
for i in range(2 ** x):
    tmp = str(bin(i)[2:]).zfill(x)
    tmp_num = S[0]
    for n in range(len(tmp)):
        if tmp[n] == '1':
            ans += int(tmp_num)
            tmp_num = S[n + 1]
        else:
            tmp_num += S[n + 1]
    ans += int(tmp_num)
print(ans)