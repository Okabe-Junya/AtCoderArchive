def base_n(num_10): # num_10: 10進数, n: 基数
    str_n = ''
    while num_10:
        if num_10 % 9 >= 10:
            return -1
        str_n += str(num_10 % 9)
        num_10 //= 9
    return int(str_n[::-1])

def base_10(num_n, n): # num_n: n進数, n: 基数
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10

n, k = map(int, input().split())
if n == 0:
    print(0)
    exit()
num_10 = n
for _ in range(k):
    num_10 = base_10(num_10, 8)
    num_9 = base_n(num_10)
    s = list(str(num_9))
    for idx in range(len(s)):
        if s[idx] == "8":
            s[idx] = "5"
    num_10 = int("".join(s))
print(num_10)