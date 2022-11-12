N = int(input())
S = set()
s1 = set(["H", "D", "C", "S"])
s2 = set(["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"])
flag = False
for _ in range(N):
    s = input()
    if s[0] in s1 and s[1] in s2:
        S.add(s)
    else:
        flag = True
if flag:
    print("No")
    exit()
if len(S) == N:
    print("Yes")
else:
    print("No")
