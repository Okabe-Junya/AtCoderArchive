# 数値→アルファベット
def num2alpha(num):
    if num <= 26:
        return chr(64+num)
    elif num % 26 == 0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num % 26)


n = int(input())
ans = num2alpha(n)
print(ans.lower())
