n = int(input())
num = list(map(int,input().split()))
ave = sum(num) // len(num)
for i in num:
  if i - ave > 0:
    print(i - ave)
  else:
    print(ave - i)