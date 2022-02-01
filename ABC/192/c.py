def a(l):
    n_max = ''
    n_min = ''
    l.sort(reverse=True)
    for j in range(len(l)):
        n_max += l[j]
        n_min += l[len(l)-1-j]
    n1 = int(n_max) - int(n_min)
    n_l = list(str(n1))
    return n_l


n, k = map(int, input().split())
n_l = list(str(n))
for i in range(k):
    n_l = a(n_l)
for i in n_l:
    print(int(i), end='')
