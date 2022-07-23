N = int(input())

dict = {}
for _ in range(N):
    s = input()
    if s in dict:
        print(s + "(" + str(dict[s]) + ")")
        dict[s] += 1
    else:
        print(s)
        dict[s] = 1