import itertools
input()
mans=list(map(int, input().split()))
print(sum(itertools.accumulate(sorted(mans))))
