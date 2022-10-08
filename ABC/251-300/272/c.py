N = int(input())
A = list(map(int, input().split()))
if len(A) == 2:
    if sum(A) % 2 == 0:
        print(sum(A))
    else:
        print(-1)
else:
    odd = []
    even = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    odd.sort(reverse=True)
    even.sort(reverse=True)
    omax = 0
    emax = 0
    if len(odd) >= 2:
        omax = odd[0] + odd[1]
    if len(even) >= 2:
        emax = even[0] + even[1]
    print(max(omax, emax))
