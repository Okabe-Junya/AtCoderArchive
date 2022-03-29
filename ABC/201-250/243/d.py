N, X = map(int, input().split())
S = input()

Stack = []
for i in S:
    if len(Stack) == 0:
        Stack.append(i)
        continue
    if (i == "U" and Stack[-1] != "U"):
        Stack.pop()
    else:
        Stack.append(i)

# print(Stack)
for i in Stack:
    if i == "S":
        continue
    elif i == "U":
        X //= 2
    elif i == "R":
        X = X * 2 + 1
    else:
        X = X * 2
print(X)    