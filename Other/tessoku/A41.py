N = int(input())
S = input()
for i in range(len(S) - 2):
    if S[i:i + 3] == "BBB" or S[i:i + 3] == "RRR":
        print("Yes")
        exit()
print("No")
