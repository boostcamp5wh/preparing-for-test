f = open('input.txt', 'r')
input = f.readline
n=int(input())
times=sorted(list(map(int, input().split())))
answer, total = 0, 0
for t in times:
    total+=t
    answer+=total
print(answer)
