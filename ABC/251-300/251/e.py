N = int(input())
A = list(map(int, input().split()))

    
check = [False] * N
ans2 = 0
start = A.index(min(A))
cur = start
check[cur] = True
check[(cur + 1) % N] = True
ans2 += A[cur]
cur += 1
cur %= N
while start != cur:
    if not check[cur]:
        check[cur] = True
        check[(cur + 1) % N] = True
        ans2 += A[cur % N]
    else:
        if check[(cur + 1) % N]:
            break
        if A[cur] + A[(cur + 2) % N] <= A[(cur + 1) % N]:
            check[(cur + 1) % N] = True
            ans2 += A[cur] 
            if not check[(cur + 2) % N]:
                ans2 += A[(cur + 2) % N]
                check[(cur + 2) % N] = True
                check[(cur + 3) % N] = True
                cur += 2
    cur += 1
    cur %= N
    
print(ans2)