N, K = map(int, input().split())
S = input()
print("Yes" if (S.count("1") - K) % 2 == 0 else "No")
