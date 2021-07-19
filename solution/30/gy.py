def solution(n, k, cmd):
    ptr = [[i-1, i+1] for i in range(n)]
    deleted = []
    for line in cmd:
        if line[0] == "C":
            deleted.append(k)
            
            before, after = ptr[k]
            
            if before >= 0:
                ptr[before][1] = after
            
            if after < n:
                ptr[after][0] = before
                
            k = after if after != n else before
        elif line[0] == "Z":
            recover_id = deleted.pop()
            before, after = ptr[recover_id]
            
            if before >= 0:
                ptr[before][1] = recover_id
            
            if after < n:
                ptr[after][0] = recover_id
        else:
            dir, x = line.split()
            dir = "UD".index(dir)
            x = int(x)
            
            for _ in range(x):
                k = ptr[k][dir]
    
    answer = ['O'] * n
    for idx in deleted:
        answer[idx] = 'X'
    return ''.join(answer)
