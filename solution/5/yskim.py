import sys
n = sys.stdin.readline()
nums = tuple(map(int, sys.stdin.readline().split()))
opers = list(map(int,sys.stdin.readline().split()))
operations = (lambda a,b:a+b, lambda a,b:a-b, lambda a,b:a*b, lambda a,b:a//b if a>0 else -(-a//b))
value=nums[0]
result=set()
def dfs(nums, value, opers, i=1):
    global result
    for o in range(4):
        if opers[o]:
            opers[o] -= 1
            newvalue = operations[o](value, nums[i])
            dfs(nums, newvalue, opers, i+1)
            opers[o] += 1
    if not sum(opers):
        result.add(value)
dfs(nums, value, opers)
print(max(result), min(result))
