n = int(input())
a = list(map(int, input().split()))
new_a = sorted(a, reverse=True)
alice = new_a[0::2]
bob = new_a[1::2]
print(sum(alice) - sum(bob))
