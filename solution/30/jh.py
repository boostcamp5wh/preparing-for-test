def solution(n, k, cmd):
    table=['O' for i in range(n)]
    stack=[]
    for do in cmd:
        if 'U'==do[0]:
            for cnt in range(int(do.split()[1])):
                while table[k-1]=='X': k-=1
                k-=1
        elif 'D'==do[0]:
            for cnt in range(int(do.split()[1])):
                k = table.index('O', k+1)
        elif 'C'==do[0]:
            stack.append(k)
            table[k]='X'
            try:
                k = table.index('O', k+1)
            except:
                while table[k]=='X': k-=1
        elif 'Z'==do[0]: table[stack.pop()]='O'
    return ''.join(table)
# 테스트 1 〉	통과 (171.88ms, 22.7MB)
# 테스트 2 〉	통과 (166.01ms, 22.7MB)
# 테스트 3 〉	통과 (163.15ms, 22.6MB)
# 테스트 4 〉	통과 (144.06ms, 29.7MB)
# 테스트 5 〉	통과 (137.51ms, 29.8MB)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)

def solution(n, k, cmd):
    table=['O' for i in range(n)]
    nums=[i for i in range(n)]
    stack=[]
    for do in cmd:
        if 'U'==do[0]: k-=int(do.split()[1])
        elif 'D'==do[0]: k+=int(do.split()[1])
        elif 'C'==do[0]:
            val=nums.pop(k)
            stack.append((k, val))
            if k==len(nums): k-=1
            table[val]='X'
        elif 'Z'==do[0]:
            idx, val=stack.pop()
            if val<nums[k]: k+=1
            nums.insert(idx, val)
            table[val]='O'
    return ''.join(table)
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (시간 초과)
# 테스트 7 〉	통과 (767.84ms, 31.9MB)
# 테스트 8 〉	통과 (3548.56ms, 36MB)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (시간 초과)
