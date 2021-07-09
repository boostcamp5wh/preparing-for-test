def solution(info, query):
    tab_a = {'cpp':0, 'java':1, 'python':2, '-':3}
    tab_b = {'backend':0, 'frontend':1,
             'junior':0, 'senior':1,
             'chicken':0, 'pizza':1, '-':2}
    trans = lambda x: x.replace(' and', '').split()
    case=[[] for _ in range(4*3*3*3)]
        
    for person in info:
        A, B, C, D, score = trans(person)
        A, B, C, D, score = tab_a[A], tab_b[B], tab_b[C], tab_b[D], int(score)
        case[A*27+B*9+C*3+D].append(score)
        case[3*27+B*9+C*3+D].append(score)
        case[A*27+2*9+C*3+D].append(score)
        case[A*27+B*9+2*3+D].append(score)
        case[A*27+B*9+C*3+2].append(score)
        case[3*27+2*9+C*3+D].append(score)
        case[3*27+B*9+2*3+D].append(score)
        case[3*27+B*9+C*3+2].append(score)
        case[A*27+2*9+2*3+D].append(score)
        case[A*27+2*9+C*3+2].append(score)
        case[A*27+B*9+2*3+2].append(score)
        case[3*27+2*9+2*3+D].append(score)
        case[3*27+2*9+C*3+2].append(score)
        case[3*27+B*9+2*3+2].append(score)
        case[A*27+2*9+2*3+2].append(score)
        case[3*27+2*9+2*3+2].append(score)
        

    case = [sorted(i) for i in case]
    
    answer=[]
    for q in query:        
        A, B, C, D, target = trans(q)
        A, B, C, D, target = tab_a[A], tab_b[B], tab_b[C], tab_b[D], int(target)
        
        idx = A*27+B*9+C*3+D
        s, e = 0, len(case[idx])-1
        while 1:
            if s>e: break
            mid = (s+e)//2
            if case[idx][mid]<target: s = mid+1
            else: e = mid-1
        answer.append(len(case[idx])-s)

    return answer
