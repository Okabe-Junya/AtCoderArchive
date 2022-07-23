N, C = map(int, input().split())
Tl = []
Al = []
tmp = C
for i in range(N):
    T, A = map(int, input().split())
    Tl.append(T)
    if T == 1:
        tmp = tmp & A
        Al.append(tmp)
    elif T == 2:
        tmp = tmp | A
        Al.append(tmp)
    else:
        Al.append(tmp ^ A)
        tmp = tmp ^ A
        


tmp = C
for i in range(N):
    if Tl[i] == 1:
        tmp = tmp & Al[i]
    elif Tl[i] == 2:
        tmp = tmp | Al[i]
    else:
        tmp =  Al[i]
    print(tmp)