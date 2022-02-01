n = int(input())
a = [input() for i in range(n)]
a = set(a)
for s in a:
    if ('!' + s) in a:
        print(s)
        break
else:
    print('satisfiable')
