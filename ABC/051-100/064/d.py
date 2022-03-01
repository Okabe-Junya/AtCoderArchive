N = int(input())
S = input()
s = []
for char in S:
    if char == "(":
        s.append(1)
    else:
        s.append(-1)

p = 0
cnt = 0
for i in range(N):
    cnt += s[i + p]
    if cnt < 0:
        s.insert(0, 1)
        p += 1
        cnt += 1

sum1 = 0
sum2 = 0
#print(s)
for i in s:
    if i == 1:
        sum1 += 1
    else:
        sum2 += 1

for _ in range(max(0, sum1 - sum2)):
    s.append(-1)

ans = ""
for i in s:
    if i == 1:
        ans += "("
    else:
        ans += ")"
print(ans)