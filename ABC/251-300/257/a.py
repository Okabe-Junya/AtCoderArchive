N, X = map(int, input().split())
alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
l = []
for i in range(len(alp)):
    for j in range(N):
        l.append(alp[i])
    
print(l[X - 1].upper())