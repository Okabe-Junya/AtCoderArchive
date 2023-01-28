S = input()
T = input()

ss = S[len(S) - len(T):]
diff = set()
for i in range(len(T)):
    if ss[i] == "?" or T[i] == "?" or ss[i] == T[i]:
        continue
    else:
        diff.add(i)

if len(diff) == 0:
    print("Yes")
else:
    print("No")

ss = list(ss)
T = list(T)

for i in range(len(T)):
    diff.discard(i)
    ss[i] = S[i]
    if not (ss[i] == "?" or T[i] == "?" or ss[i] == T[i]):
        diff.add(i)

    # print(ss, T, diff)
    if len(diff) == 0:
        print("Yes")
    else:
        print("No")
