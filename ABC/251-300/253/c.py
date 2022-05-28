Q = int(input())
dict = {}
for _ in range(Q):
    s = list(input().split())
    if s[0] == '1':
        if int(s[1]) in dict:
            dict[int(s[1])] += 1
        else:
            dict[int(s[1])] = 1
    elif s[0] == '2':
        if int(s[1]) in dict:
            dict[int(s[1])] -= int(s[2])
            if dict[int(s[1])] <= 0:
                del dict[int(s[1])]
    else:
        print(max(dict) - min(dict))