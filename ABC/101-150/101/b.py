n = int(input())
s = list(str(n))
s_n = 0  # 各位の和
for i in s:
    s_n += int(i)
if n % s_n == 0:
    print('Yes')
else:
    print('No')