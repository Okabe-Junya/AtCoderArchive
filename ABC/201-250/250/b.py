N, A, B = map(int, input().split())
if N % 2 == 0:
    patA = ("." * B + "#" * B) * (N // 2)
    patB = ("#" * B + "." * B) * (N // 2)
else:
    patA = ("." * B + "#" * B) * (N // 2) + "." * B
    patB = ("#" * B + "." * B) * (N // 2) + "#" * B
for i in range(N):
    for j in range(A):
        if i % 2 == 0:
            print(patA)
        else:
            print(patB)
            