n=int(input())
nums = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
M, m = -1000000000, 1000000000

def dfs(plus, minus, multi, div, step, result):
    global nums, M, m, n
    if step==n:
        M, m = max(M, result), min(m, result)
        return 0
        
    if plus: dfs(plus-1, minus, multi, div, step+1, result+nums[step])
    if minus: dfs(plus, minus-1, multi, div, step+1, result-nums[step])
    if multi: dfs(plus, minus, multi-1, div, step+1, result*nums[step])
    if div:
        if result>0: dfs(plus, minus, multi, div-1, step+1, result//nums[step])
        else: dfs(plus, minus, multi, div-1, step+1, -(abs(result)//nums[step]))

dfs(plus, minus, multi, div, 1, nums[0])
print(M, m, sep='\n')
