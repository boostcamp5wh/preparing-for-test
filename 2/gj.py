n = int(input())
aa = list(map(int, input().split()))
b, c = list(map(int, input().split()))

total = 0
for a in aa:
    total += 1 + (max(a-b, 0) + c - 1) // c
print(total)
