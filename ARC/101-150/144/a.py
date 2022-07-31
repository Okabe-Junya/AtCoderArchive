N = int(input())
print(2 * N)
ans = ""
while N >= 4:
    ans += "4"
    N -= 4
if N != 0:
    ans += str(N)

reversed_ans = ans[::-1]
print(reversed_ans)