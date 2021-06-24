n = int(input())
ps = list(map(int, input().split()))
ps.sort(reverse=True)
total = 0
for idx, v in enumerate(ps):
    total += v * (idx + 1)
print(total)
