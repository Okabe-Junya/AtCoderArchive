n, m = map(int, input().split())
s = list(input().split())
t = list(input().split())

rapid = set(t)
for i in s:
    if i in rapid:
        print("Yes")
    else:
        print("No")