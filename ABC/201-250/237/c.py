import sys

s = input()
if str(s) == str(s)[::-1]:
    print("Yes")
    sys.exit()

i = 0
l = 0
r = 0
while s[i] == "a":
    l += 1
    i += 1
i = -1
while s[i] == "a":
    i -= 1
    r += 1
s = s.lstrip("a")
s = s.rstrip("a")
if (str(s) == str(s)[::-1]) & (l <= r):
    print("Yes")
    sys.exit()
print("No")
