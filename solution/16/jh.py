def solution(info, query):
    tab_a={'cpp':1, 'java':2, 'python':4, '-':7}
    tab_b={'backend':1, 'frontend':2,
           'junior':1, 'senior':2,
           'chicken':1, 'pizza':2, '-':3}
    trans = lambda x: x.replace(' and', '').split()
    
    answer=[]
    for q in query:
        A, B, C, D, E = trans(q)
        A, B, C, D, E = tab_a[A], tab_b[B], tab_b[C], tab_b[D], int(E)
        cnt=0
        for person in info:
            a, b, c, d, e = trans(person)
            a, b, c, d, e = tab_a[a], tab_b[b], tab_b[c], tab_b[d], int(e)
            if A&a and B&b and C&c and D&d and E<=e: cnt+=1
        answer.append(cnt)
    return answer
