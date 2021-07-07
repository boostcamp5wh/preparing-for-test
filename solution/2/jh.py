from math import ceil
input()
nums=list(map(int, input().split()))
b, c = map(int, input().split())
answer=0
for num in nums:
    if num-b>0: answer+=ceil((num-b)/c)+1
    else: answer+=1
print(answer)
