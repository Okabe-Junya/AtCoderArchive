N = int(input())
S = input()
l = []
for char in S:
    if char == "(":
        l.append(1)
    else:
        l.append(-1)

cnt = 0
for num in l:
    cnt += num
    if cnt < 0:
        print("No")
        break
else:
    if cnt == 0:
        print("Yes")
    else:
        print("No")